import pytest
from functions_ttt import *


def test_check_game_win_tricky_board():
    board = ['O', 'O', 'X', 'O', 'X', 'X', 'X', '.', '.']
    is_win, player = check_win(board)
    assert (player == 'X')


def test_get_current_turn():
    board = ['X', 'O', 'X', 'O', 'O', 'X', 'X', 'X', '.']
    turn_no = get_current_turn_number(board)
    assert (turn_no == 9)


def test_get_current_player():
    board = ['X', '.', '.', '.', 'X', 'O', '.', '.', 'O']
    current_player = get_current_player(board)
    assert (current_player == 'Xgit p')


def test_play_turn():
    # tries to put a character on an already taken position
    board = ['O', '.', 'X', 'X', 'X', '.', 'O', '.', '.']
    row = 1
    col = 1
    is_valid, board_output = play_turn(board, row, col)
    assert (not is_valid)


def test_check_draw():
    board = ['X', 'O', 'O', 'X', 'X', 'O', 'O', 'X', 'O']
    is_draw = check_draw(board)
    assert is_draw


def test_check_win():
    board = ['X', '.', 'O', '.', 'X', 'O', '.', '.', 'X']
    is_win, player_win = check_win(board)
    assert (player == 'X')