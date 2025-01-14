import tkinter as tk
from tkinter import messagebox

def check_winner():
    """Check if there's a winner or a draw."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # Check for a draw
    for row in board:
        if " " in row:
            return None

    return "Draw"

def on_click(row, col):
    global current_player
    if board[row][col] == " " and not game_over:
        board[row][col] = players[current_player]
        buttons[row][col].config(text=players[current_player])

        result = check_winner()
        if result:
            end_game(result)
        else:
            current_player = 1 - current_player


def end_game(result):
    global game_over
    game_over = True
    if result == "Draw":
        messagebox.showinfo("Game Over", "It's a draw!")
    else:
        messagebox.showinfo("Game Over", f"Player {result} wins!")

def reset_game():
    global board, current_player, game_over
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = 0
    game_over = False
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ")

# Initialize the game
root = tk.Tk()
root.title("Tic Tac Toe")

players = ["X", "O"]
current_player = 0
board = [[" " for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
game_over = False

# Create the UI buttons
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text=" ", font=("Arial", 24), width=5, height=2,
                                      command=lambda r=row, c=col: on_click(r, c))
        buttons[row][col].grid(row=row, column=col)

# Add a reset button
reset_button = tk.Button(root, text="Reset", font=("Arial", 16), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

root.mainloop()
