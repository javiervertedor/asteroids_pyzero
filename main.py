"""
    _    ____ _____ _____ ____   ___ ___ ____  ____  
   / \  / ___|_   _| ____|  _ \ / _ \_ _|  _ \/ ___| 
  / _ \ \___ \ | | |  _| | |_) | | | | || | | \___ \ 
 / ___ \ ___) || | | |___|  _ <| |_| | || |_| |___) |
/_/   \_\____/ |_| |_____|_| \_\\___/___|____/|____/ 

Arcade Asteriods game created with PyGame Zero and PGHelper

TO DO:
    - Splash screen
    - Play again?
    - Center the game screen
"""

import random
import time
import pgzrun
from pgzhelper import *

WIDTH = 800
HEIGHT = 600

# globals
score = 0
health = 19
health_holdoff = 0
powerup_time = 0
game_over_played = False

lasers = []
laser_holdoff = 0
laser_hit_idx = 0

music.play('music1')


# local helper functions
def rotate(actor):
    if actor.angle == 360:
        actor.angle = 0
    else:
        actor.angle += 1


def relocate(actor, scale=1):
    # Avoid ship
    x = ship.x
    y = ship.y
    while (x == ship.x) and (y == ship.y):
        x = random.randint(20, 780)
        y = random.randint(20, 580)
    actor.x = x
    actor.y = y
    actor.scale = scale
    actor.direction = random.randint(0, 359)


background = Actor('spacebg')

health_bar = Actor(f'health{health}')
health_bar.scale = 0.8
health_bar.x = 140
health_bar.y = 30

ship = Actor('playership')
ship.images = [ship.image, 'playership_damage']
ship.fps = 10
ship.y = 550
ship.x = 400

meteors = [Actor('meteorbrown1'), Actor('meteorbrown2'), Actor('meteorbrown3'),
           Actor('meteorbrown4'), Actor('meteorgrey1'), Actor('meteorgrey2'),
           Actor('meteorgrey3'), Actor('meteorgrey4')]

for meteor in meteors:
    relocate(meteor, round(random.uniform(0.5, 1.5), 1))

explosions = []
powerups = []


def on_mouse_move(pos, rel, buttons):
    ship.x = pos[0]
    ship.y = pos[1]


def on_mouse_down(pos, button):
    global lasers, laser_holdoff
    if button == 1:
        if laser_holdoff == 0:
            sounds.laser.play()
            laser = Actor('laser')
            laser.angle = 90
            laser.x = ship.x
            laser.y = ship.y - 30
            lasers.append(laser)
            laser_holdoff = 1
        else:
            laser_holdoff -= 1

def update():
    global score, health, health_holdoff, laser_hit_idx, powerup_time

    health_bar.image = f'health{health}'
    health_bar.scale = 0.8
    health_bar.x = 140
    health_bar.y = 30

    # meteors
    for meteor in meteors:
        rotate(meteor)
        meteor.move_in_direction(round(random.uniform(0.5, 1.5), 1))  # meteor speed

        # meteor collisions
        if meteor.collidelist(lasers) != -1:
            try:
                del lasers[laser_hit_idx]
            except IndexError:
                pass
            finally:
                explotion = Actor('explosion_1')
                explotion.images = [explotion.image, 'explosion_2', 'explosion_3',
                                    'explosion_4', 'explosion_5', 'explosion_6', 'explosion_7',
                                    'explosion_8', 'explosion_9', 'explosion_10']
                explotion.x = meteor.x
                explotion.y = meteor.y
                explotion.scale = 0.5
                explotion.fps = 10
                explosions.append(explotion)
                sounds.explosion.play()
                score += 1
                relocate(meteor, round(random.uniform(0.5, 1.5), 1))

        if (meteor.x > 800) or (meteor.y > 600) or (meteor.x < 0) or (meteor.y < 0):
            relocate(meteor, round(random.uniform(0.5, 1.5), 1))

    for explotion in explosions:
        if explotion.animate() >= 9:
            explosions.remove(explotion)

    # ship collides with meteors
    if ship.collidelist(meteors) != -1:
        ship.animate()
        if health_holdoff == 0:
            if health > 0:
                health -= 1
                sounds.loose.play()
                health_holdoff = 50
        else:
            health_holdoff -= 1
    else:
        ship.image = 'playership'

    # laser collisions
    for idx, laser in enumerate(lasers):
        if laser.y > 595:
            lasers.remove(laser)
        elif laser.collidelist(meteors) != -1:
            laser_hit_idx = idx
        else:
            laser.y -= 5

    # Power Up
    if health < 19 and powerup_time == 0:
        # TO DO: fix random time - use a counter with random values: powerup_time
        powerup = Actor('powerup')
        relocate(powerup)
        powerups.append(powerup)
        powerup_time = random.randint(100, 300)

    if powerup_time > 0:
        powerup_time -= 1

    for powerup in powerups:
        powerup.move_in_direction(round(random.uniform(0.5, 1.5), 1))  # powerup speed
        # detect collision with ship
        if powerup.colliderect(ship):
            powerups.remove(powerup)
            sounds.powerup.set_volume(4)
            sounds.powerup.play()
            health += 1
            if health > 19:
                health = 19
        # remove if outside the screen
        elif (powerup.x > 800) or (powerup.y > 600) or (powerup.x < 0) or (powerup.y < 0):
            powerups.remove(powerup)

def draw():
    global game_over_played, powerup_time
    screen.fill((0, 0, 0))
    background.draw()
    health_bar.draw()
    if health > 0:
        screen.draw.text(f'Score: {score}', (330, 18), color=(255, 255, 255), fontsize=40)

        for meteor in meteors:
            meteor.draw()

        for explotion in explosions:
            explotion.draw()

        for powerup in powerups:
            powerup.draw()

        ship.draw()

        for laser in lasers:
            laser.draw()
    else:
        powerup_time = -1
        powerups.clear()
        meteors.clear()
        explosions.clear()
        lasers.clear()
        screen.draw.text(f'Score: {score}', (250, 300), color=(245, 243, 127), fontsize=100)
        screen.draw.text('Game Over', (220, 450), color=(255, 255, 255), fontsize=100)
        music.stop()
        if not game_over_played:
            sounds.game_over.play()
            game_over_played = True


# Main loop
pgzrun.go()