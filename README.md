# 🐍 Snake Game

A classic Snake game built with **Python** and **Pygame**. Control the snake, eat the apples, grow longer, and avoid hitting the walls or yourself!

## Features

- Smooth grid-based movement (640x480 window)
- Snake head with eyes that follow the direction of movement
- Darker tail and lighter body segments
- Live score counter
- Game over screen with quick restart
- Arrow keys and WASD controls

## Requirements

- Python 3.8 or higher
- Pygame

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. (Optional) Create a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the game

```bash
python snake_game.py
```

On macOS / Linux, use `python3 snake_game.py` if `python` does not work.

## Controls

| Key              | Action                        |
| ---------------- | ----------------------------- |
| `↑` or `W`       | Move up                       |
| `↓` or `S`       | Move down                     |
| `←` or `A`       | Move left                     |
| `→` or `D`       | Move right                    |
| `SPACE`          | Restart (after game over)     |

## How to Play

1. Guide the snake to the red apple to eat it.
2. Each apple gives you **+1 point** and makes the snake longer.
3. The game ends if the snake hits a wall or its own body.
4. Press **SPACE** to play again.

## Customization

You can change these values at the top of `snake_game.py`:

| Constant        | Default | Meaning                              |
| --------------- | ------- | ------------------------------------ |
| `SCREEN_WIDTH`  | 640     | Window width                         |
| `SCREEN_HEIGHT` | 480     | Window height                        |
| `GRID_SIZE`     | 20      | Size of each cell in pixels          |
| `FPS`           | 10      | Game speed (higher = faster snake)   |

## Troubleshooting

- **`ModuleNotFoundError: No module named 'pygame'`** → run `pip install pygame`
- **`pip` not found** → try `python -m pip install pygame`
- **Window does not open** → make sure you are running on a machine with a display (not a remote server)

## License

This project is open source. Feel free to use and modify it.
