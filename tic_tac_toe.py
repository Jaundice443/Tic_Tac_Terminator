import random


def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(board[i]+board[i+1]+board[i+2])

def open_spots(board):
    spots = []
    for i in range(len(board)):
        if board[i] == '-':
            spots.append(i)
    return spots

def random_move(board, symbol):
    spots = open_spots(board)
    idx = random.choice(spots)
    board[idx] = symbol

def check_three(board, idx1, idx2, idx3):
    if board[idx1] == board[idx2] == board[idx3] and board[idx1] != '-':
        return board[idx1]
    else:
        return '-'

def winner(board):
    combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]]
    for combo in combos:
        win_symbol = check_three(board, combo[0], combo[1], combo[2])
        if win_symbol != '-':
            return win_symbol
    if open_spots(board) == []:
        return 'D'
    else:
        return '-'

def tic_tac_toe():
    board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    win = '-'
    turn = 'X'
    while win == '-':
        if turn == 'X':
            random_move(board, turn) #X plays randomly
            turn = 'O'
        else:
            #O plays perfectly
            best_val = 100
            best_idx = None
            for i in open_spots(board):
                board_copy = board[:]
                board_copy[i] = "O" #Simulate move on copy, see what happens
                result = force_win(board_copy)
                if result < best_val:
                    best_val = result
                    best_idx = i
            
            board[best_idx] = "O" #Makes ideal move
            turn = 'X'
        win = winner(board)
    return win

def play_games(n):
    wins = {'X':0, 'O':0, 'D':0}
    for i in range(n):
        win_symbol = tic_tac_toe()
        wins[win_symbol] += 1
    print("X wins:", wins['X'])
    print("O wins:", wins['O'])
    print("Draws:", wins['D'])

#Problem C

def force_win(board):
    #1 if X has won or can force a win
    #-1 if O has won or can force a win
    #0 if the game will end in a draw

    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    elif winner(board) == "D":
        return 0
    else:
        if len(open_spots(board)) % 2 == 1:
            symbol = "X"
            best_val = -float("inf")
        else:
            symbol = "O"
            best_val = float("inf")
        #Recursive call for each space
        for i in open_spots(board):
            board_copy = board[:]
            board_copy[i] = symbol
            value = force_win(board_copy)

            if symbol == "X":
                if value > best_val:
                    best_val = value
            else:
                if value < best_val:
                    best_val = value
    
    return best_val
        
if __name__ == '__main__':
    print()
    #Base Cases: Game already over
    print(force_win(['O','X','O',
                     'X','X','O',
                     'X','O','X'])) #0 (Draw)

    print(force_win(['X','X','O',
                     'O','X','X',
                     'O','X','O'])) #1 (X wins)

    print(force_win(['X','-','O',
                     'X','O','-',
                     'O','-','X'])) #-1 (O wins)

    #O's turn: can force tie by taking bottom left
    print(force_win(['X','O','X',
                     'X','O','-',
                     '-','X','O'])) #0

    #X's turn: can take bottom left and win
    print(force_win(['X','O','X',
                     'X','O','-',
                     '-','-','O'])) #1

    #O's turn: X can force a win on next move no matter where
    #O goes, so all of O's options result in board state 1.
    print(force_win(['-','O','-',
                     '-','X','X',
                     '-','O','X'])) #1
    
if __name__ == '__main__':

    play_games(100)

    #X never wins, some draws some wins for O