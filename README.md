# 🚀 Asteroids Arcade Game (PyGame Zero)

A classic-style Asteroids arcade shooter built with **Python**, **PyGame Zero**, and custom helper utilities. Battle waves of meteors, collect power-ups, and survive as long as possible!

![screenshot-placeholder](https://via.placeholder.com/800x600.png?text=Gameplay+Screenshot)

---

## 🎮 Features

- Mouse-controlled spaceship movement  
- Laser-based shooting system  
- Rotating and moving meteors  
- Dynamic health bar and health-based visual feedback  
- Power-up drops that restore health  
- Explosions with animations  
- Background music and sound effects  
- Game over screen with final score  

---

## 🛠️ Requirements

- Python 3.7+
- [pgzero](https://pygame-zero.readthedocs.io/en/stable/)
- pygame

Install the required dependencies:

```bash
pip install pgzero pygame
```

---

## ▶️ How to Play

1. Clone this repo or download the files.  
2. Run the game using:

```bash
pgzrun main.py
```

3. Move the ship using your mouse.  
4. Left-click to shoot lasers at meteors.  
5. Avoid or destroy meteors to stay alive.  
6. Pick up power-ups to regain health.  
7. Game ends when your health reaches zero.  

---

## 📁 File Structure

```
.
├── main.py            # Main game logic
├── pgzhelper.py       # Enhanced actor and collision utilities
├── images/            # Game sprite assets
├── sounds/            # Sound effects and background music
└── README.md          # This file
```

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

```
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

[... truncated for brevity ...]
```

---

## 🙌 Credits

- Built using [PyGame Zero](https://pygame-zero.readthedocs.io/)
- Explosion animation and sprites: [Kenney.nl](https://kenney.nl/assets)
- Sound effects and music: [freesound.org](https://freesound.org) (or your own sources)

---

## 💡 To Do

- Add splash screen  
- Add "Play Again" prompt  
- Center game screen on various displays  

---

Enjoy the retro action!
