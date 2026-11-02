# 🐍 Snake Game

A classic Snake game built with **Python** and **Pygame**. Control the snake, eat the apples, grow longer, and avoid hitting the walls or yourself!

## How to Run (For Beginners)

### Before you start

Install **Python** on your computer:

1. Go to https://www.python.org/downloads/ and download Python.
2. Run the installer and **tick the box "Add Python to PATH"** at the bottom of the first screen.
3. Click "Install Now".
4. Install **VS Code** from https://code.visualstudio.com/ if you do not have it.

To check that Python is installed, open Command Prompt and type `python --version`. You should see a version number.

### Steps

1. Open this repository page on GitHub.
2. Click the green **Code** button, then click **Download ZIP**.
3. Open your Downloads folder. You will find a file named `snake-game-python--main.zip`.
4. Right-click on the zip file and click **Extract All**.
5. Move the extracted folder to your **C: drive** (or Desktop).
6. Open **VS Code**.
7. Press `Ctrl + Shift + E` to open the Explorer panel.
8. Click **Open Folder**.
9. Select the extracted folder `snake-game-python--main` and click **Select Folder**.
10. Open the terminal in VS Code by pressing `` Ctrl + ` `` (the backtick key, just below the Esc key).
11. You will see a path like this in the terminal:

    C:\snake-game-python--main

12. If you see a second folder with the same name inside, go into it by typing:

    cd snake-game-python--main

    Now the path should look like this:

    C:\snake-game-python--main\snake-game-python--main

    Make sure you can see the files `snake_game.py` and `requirements.txt` in this folder.

13. Install the required library by typing:

    pip install -r requirements.txt

14. Start the game by typing:

    python snake_game.py

15. The game window will open. Enjoy the game! 🎮

### Common problems

- **'python' is not recognized** → Python is not added to PATH. Reinstall Python and tick "Add Python to PATH".
- **'pip' is not recognized** → Try `python -m pip install -r requirements.txt`.
- **No such file or directory: requirements.txt** → You are in the wrong folder. Use the `cd` command (step 12) until you see `snake_game.py` in the folder.

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
