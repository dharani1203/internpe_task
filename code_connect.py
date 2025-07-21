import os

# Setup board
rows = 6
cols = 7
gameBoard = [["" for _ in range(cols)] for _ in range(rows)]
possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def printGameBoard():
    print("\n     A    B    C    D    E    F    G")
    for x in range(rows):
        row = rows - 1 - x  # Reverse row index for display
        print("   +----+----+----+----+----+----+----+")
        print(f"{row}  |", end="")
        for y in range(cols):
            cell = gameBoard[row][y]
            if cell == "🔵" or cell == "🔴":
                print(f" {cell} ", end="|")
            else:
                print("    ", end="|")
        print()
    print("   +----+----+----+----+----+----+----+")

def is_column_full(col):
    return gameBoard[0][col] != ""

def drop_piece(col, player):
    for row in range(rows - 1, -1, -1):
        if gameBoard[row][col] == "":
            gameBoard[row][col] = player
            return row, col  # Return the location of the placed piece
    return None, None

def get_player(turn):
    return "🔵" if turn % 2 == 0 else "🔴"

def check_winner(player):
    # Horizontal
    for row in range(rows):
        for col in range(cols - 3):
            if all(gameBoard[row][col + i] == player for i in range(4)):
                return True

    # Vertical
    for col in range(cols):
        for row in range(rows - 3):
            if all(gameBoard[row + i][col] == player for i in range(4)):
                return True

    # Diagonal ↘
    for row in range(rows - 3):
        for col in range(cols - 3):
            if all(gameBoard[row + i][col + i] == player for i in range(4)):
                return True

    # Diagonal ↗
    for row in range(3, rows):
        for col in range(cols - 3):
            if all(gameBoard[row - i][col + i] == player for i in range(4)):
                return True

    return False

def play_game():
    turn = 0
    while True:
        clear_screen()
        printGameBoard()
        current_player = get_player(turn)
        print(f"\nPlayer {current_player}'s turn.")
        move = input("Choose a column (A-G): ").upper()

        if move not in possibleLetters:
            print("Invalid input. Please choose a letter from A to G.")
            input("Press Enter to try again...")
            continue

        col = possibleLetters.index(move)

        if is_column_full(col):
            print("That column is full. Choose another.")
            input("Press Enter to try again...")
            continue

        row, col = drop_piece(col, current_player)

        if check_winner(current_player):
            clear_screen()
            printGameBoard()
            print(f"\n🏆 Player {current_player} wins! 🏆")
            break

        turn += 1

# Start the game
play_game()

