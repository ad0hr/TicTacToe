def initialise_board():
    """ makes an empty 3x3 table to use as the tic-tac-toe board
        Arguments:
        Returns: board_list (list), contains 9 strings of . to represent an empty 3x3 board
        Notes: no pre- or post-conditions required."""
    board_list = ['.', '.', '.', '.', '.', '.', '.', '.', '.']
    return board_list


def display_board(board_list):
    """ displays the 3x3 tic-tac-toe board
        Arguments: board_list (list), holds the list of characters in the board
        Returns:
        Notes: the function will display whatever the board input is, so recent changes are taken into consideration"""
    print(board_list[0:3])
    print(board_list[3:6])
    print(board_list[6:9])


def get_current_turn_number(board_list):
    """ uses the board to determine the number of turns
        Arguments: board_list (list), holds the list of characters in the board
        Returns: turn_number (integer), represents the current number of turns
        Notes: goes through the entire board list one by one to count the number of turns"""
    turn_number = 1
    for current_turn_number in board_list:
        if current_turn_number != '.':
            turn_number += 1
    return turn_number


def get_current_player(board_list):
    """ uses the board to determine the current player
        Arguments: board_list (list), holds the list of characters in the board
        Returns: O (string), which represents that the current player is O
                X (string), which represents that the current player is X
        Notes: there are only two players, O and X and X will always be the first player"""
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
    """ places a character on the board, using a row and column position
        Argument: board_list (list), holds the list of characters in the board
                row (int), row that the character will be placed onto on the board
                col (int), column that the character will be placed onto on the board
        Returns: True (boolean), if the turn is valid-the position that the character is to be placed on was
                originally empty
                False (boolean), to be returned if the turn is invalid-the new position the character is to be placed
                on is taken
                board_list (list),
                if the turn is valid-the updated board with the addition of the new character
                if turn is invalid-the same board as the input
        Notes: Can only pick from rows 1-3 and columns 1-3 due to the 3x3 nature of board
            uses the previous function get_current_player
        """
    row = int(row)
    col = int(col)
    i = (3 * (row - 1)) + col - 1
    # mathematical used to output the row and column numbers with the corresponding list index
    if board_list[i] == '.':
        if get_current_player(board_list) == 'O':
            # use of previous function helps to know which character should be placed; either O or X
            board_list[i] = 'O'
            return True, board_list
        else:
            board_list[i] = 'X'
            return True, board_list
    else:
        # ^the position is taken by a character already and the move is invalid,hence the false return
        return False, board_list


def check_draw(board_list):
    """ checks if there is a draw
        Arguments: board_list (list), holds the list of characters in the board
        Returns: True (boolean), if there is a draw
                False (boolean), there is no draw
        Notes: uses previous function get_current_turn_number"""
    if get_current_turn_number(board_list) == 10:
        # if the number of turns gets to 10, all the places have been taken up with no winner, so there will
        # inevitably be a draw
        return True
    else:
        return False


def check_win(board_list):
    """ checks if there is a win in the board, and which player was the winner
        Arguments: board_list (list), holds the list of characters in the board
        Returns: True (boolean), there is a win in the board
                False (boolean), there is no win in the board
                O (string), the winner is player O
                X (string), the winner is player X
        Notes: function checks for all possible winning combinations and returns if the winning combination is met"""
    # while loop goes through every element in board_list
    if ((board_list[0:3]) or (board_list[3:6]) or (board_list[6:9])) == ['X', 'X', 'X']:
        # checking for X win across all rows
        return True, 'X'
    elif ((board_list[0:3]) or (board_list[3:6]) or (board_list[6:9])) == ['O', 'O', 'O']:
        # checking for O win across all rows
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
    """ uses user input to play tic-tac-toe
        Arguments:
        Returns:
        Notes: No arguments or returns as the function wholly depends on user input
            This function uses all previous functions
        Example: The function will print all beginning instructions, and initialise the board
                It will only need a row and column input each 'turn' to change the board
                It will also check for winning combinations and draws
                So the game will announce a winner, or a draw when obtained
                Game will also not allow invalid turns (new position has already been taken up by an O or X, will
                instead display the previous unchanged board again"""
    print('Welcome to TIC TAC TOE!\n'
          'To play, type in the desired row and column of where you want to place your character\n'
          'Make sure you only play when it\'s your turn- Player X always goes first\n'
          'Good luck!')
    board = initialise_board()
    while not check_draw(board):
        print('-----------------------------------------------------------------------------------------------\n'
              'New move!')
        display_board(board)
        get_current_turn_number(board)
        get_current_player(board)
        print('Current player:', get_current_player(board))
        print('Current turn:', get_current_turn_number(board))
        print('Input the row and column position you want your character to be placed on')
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
