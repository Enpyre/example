from enpyre import Enpyre

enpyre = Enpyre()

enpyre.x = enpyre.y = START_X = START_Y = 0
BOARD_WIDTH = BOARD_HEIGHT = 600


def draw_cherry(x, y):
    sprite = enpyre.add_sprite(
        "https://enpyre.github.io/assets/images/pacman/cherry.png"
    )
    sprite.x = x
    sprite.y = y
    sprite.width = 50
    sprite.height = 50
    return sprite


def draw_pacman(x, y):
    sprite = enpyre.add_sprite(
        "https://enpyre.github.io/assets/images/pacman/pacman.png"
    )
    sprite.x = x
    sprite.y = y
    sprite.width = 50
    sprite.height = 50
    return sprite


def start_board():
    board = []
    for x in range(BOARD_WIDTH // 100):
        board.append([])
        for y in range(BOARD_HEIGHT // 100):
            print("x", x, "y", y)
            if x == 0 and y == 0:
                board[x].append(draw_pacman(x, y))
            else:
                board[x].append(draw_cherry(x * 100, y * 100))
    enpyre.board = board
    enpyre.add_song(
        alias="evolution",
        url="https://enpyre.github.io/assets/songs/evolution.mp3",
        play_on_load=True,
    )
    return board[0][0]


def move(x, y):
    print(f"Moving to {x}, {y}")
    print(f"Current position: {enpyre.x}, {enpyre.y}")
    width = x * 100
    height = y * 100
    to_destroy = enpyre.board[x][y]
    pacman = enpyre.board[enpyre.x][enpyre.y]
    enpyre.board[enpyre.x][enpyre.y] = None
    enpyre.board[x][y] = pacman
    if to_destroy:
        to_destroy.destroy()
    pacman.x = width
    pacman.y = height
    enpyre.x = x
    enpyre.y = y


def compute_key():
    if enpyre.key_pressed(enpyre.KEY_UP):
        if enpyre.y > 0:
            move(enpyre.x, enpyre.y - 1)
    if enpyre.key_pressed(enpyre.KEY_DOWN):
        if enpyre.y < BOARD_HEIGHT // 100 - 1:
            move(enpyre.x, enpyre.y + 1)
    if enpyre.key_pressed(enpyre.KEY_LEFT):
        if enpyre.x > 0:
            move(enpyre.x - 1, enpyre.y)
    if enpyre.key_pressed(enpyre.KEY_RIGHT):
        print(f"BOARD_WIDTH: {BOARD_WIDTH}")
        print(f"BOARD_HEIGHT: {BOARD_HEIGHT}")
        if enpyre.x < BOARD_WIDTH // 100 - 1:
            move(enpyre.x + 1, enpyre.y)


def update(delta: float):
    if not hasattr(enpyre, "board"):
        start_board()
    else:
        compute_key()


enpyre.run(BOARD_HEIGHT, BOARD_WIDTH, "#ffffff", update)
