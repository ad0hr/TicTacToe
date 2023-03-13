def initialise_board():
    board_list = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
    return board_list


def display_board(board_list):
    print(board_list[0:3])
    print(board_list[3:6])
    print(board_list[6:9])


def get_current_turn_number(board_list):
    turn_number = 1
    for current_turn_number in board_list:
        if current_turn_number != '.':
            turn_number += 1
    return turn_number


def get_current_player(board_list):
    number_of_x = 1
    number_of_O = 0
    for current_turn in board_list:
        # goes through all values in the current board to see how many 0's and X's there are
        # ^this will help determine whose turn it is :)
        if current_turn == 'O':
            number_of_x += 1
        elif current_turn == 'X':
            number_of_O += 1
    if number_of_O == number_of_x:
        return 'O'
    else:
        return 'X'


def play_turn(board_list, row, col):
    row = int(row)
    col = int(col)
    i = (3 * (row - 1)) + col - 1
    if board_list[i] == '.':
        if get_current_player(board_list) == 'O':
            board_list[i] = 'O'
            display_board(board_list)
            return True, board_list
        else:
            board_list[i] = 'X'
            # display_board(board_list)
            return True, board_list
    else:
        # ^the position is taken by a character already and the move is invalid,hence the false return
        # print(display_board)
        print('Turn is invalid, please try again')
        # display_board(board_list)
        return False, board_list


def check_draw(board_list):
    if get_current_turn_number(board_list) == 10:
        return True
    else:
        return False


def check_win(board_list):
    # while loop goes through every element in board_list
    if ((board_list[0:3]) or (board_list[3:6]) or (board_list[6:9])) == ['X', 'X', 'X']:
        # checking for X win across a row
        return True, 'X'
    elif ((board_list[0:3]) or (board_list[3:6]) or (board_list[6:9])) == ['O', 'O', 'O']:
        # checking for O win across a row
        return True, 'O'
    elif board_list[0] == 'X' and board_list[3] == 'X' and board_list[6] == 'X':
        # checking for X win down leftmost column
        return True, 'X'
    elif board_list[1] == 'X' and board_list[4] == 'X' and board_list[7] == 'X':
        # checking for X win down middle column
        return True, 'X'
    elif board_list[2] == 'X' and board_list[5] == 'X' and board_list[8] == 'X':
        # checking for X win down rightmost column
        return True, 'X'
    elif board_list[0] == 'O' and board_list[3] == 'O' and board_list[6] == 'O':
        # checking for O win down leftmost column
        return True, 'O'
    elif board_list[1] == 'O' and board_list[4] == 'O' and board_list[7] == 'O':
        # checking for O win down middle column
        return True, 'O'
    elif board_list[2] == 'O' and board_list[5] == 'O' and board_list[8] == 'O':
        # checking for O win down rightmost column
        return True, 'O'
    elif board_list[0] == 'X' and board_list[4] == 'X' and board_list[8] == 'X':
        # checking for X win across the diagonals
        return True, 'X'
    elif board_list[2] == 'X' and board_list[4] == 'X' and board_list[6] == 'X':
        # checking for X win across the diagonals
        return True, 'X'
    elif board_list[0] == 'O' and board_list[4] == 'O' and board_list[8] == 'O':
        # checking for O win across the diagonals
        return True, 'O'
    elif board_list[2] == 'O' and board_list[4] == 'O' and board_list[6] == 'O':
        # checking for O win across the diagonals
        return True, 'O'
    else:
        return False, None


def play_game():
    print('Welcome to TIC TAC TOE!\n'
          'To play, type in the desired row and column of where you want to place your character\n'
          'Make sure you only play when it\'s your turn- Player X always goes first\n'
          'Good luck!')
    board = initialise_board()
    while not check_draw(board):
        print('-----------------------------------------------------------------------------------------------\n'
              'New move! Input the position you want your character to be placed on')
        display_board(board)
        get_current_turn_number(board)
        get_current_player(board)
        print('Current player:', get_current_player(board))
        print('Current turn:', get_current_turn_number(board))
        print('Row number:')
        row = input()
        print('Column number:')
        col = input()
        play_turn(board, row, col)
        win, winner = check_win(board)
        if winner == 'X':
            display_board(board)
            print('Player X has won!')
            return
        elif winner == 'O':
            display_board(board)
            print('Player O has won!')
            return
    print('There has been a draw! No one wins :(')
