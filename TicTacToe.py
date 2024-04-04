from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
player_turn = 'X'
board = []

def make_move(i, j):
    global player_turn
    if board[i][j]['text'] == ' ':
        board[i][j]['text'] = player_turn
        board[i][j]['state'] = 'disabled'
        if check_win():
            messagebox.showinfo("Game Over", f"Player {player_turn} wins!")
            root.quit()
        else:
            player_turn = 'O' if player_turn == 'X' else 'X'

def check_win():
    for i in range(3):
        if board[i][0]['text'] == board[i][1]['text'] == board[i][2]['text'] != ' ':
            return True
        if board[0][i]['text'] == board[1][i]['text'] == board[2][i]['text'] != ' ':
            return True
    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != ' ':
        return True
    if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != ' ':
        return True
    return False

for i in range(3):
    row = []
    for j in range(3):
        button = Button(root, text=' ', command=lambda i=i, j=j: make_move(i, j), height=3, width=6, bg = 'black')
        button.grid(row=i, column=j)
        row.append(button)
    board.append(row)

root.mainloop()
