def check_for_empty(string):
    """
    This function would replace a blank string with a single space.
    :param string: String which is to be checked if it is empty.
    :return: If string is blank, a space is returned, otherwise string is returned as is.
    """
    if string == "":
        return " "
    else:
        return string


def display_board(position_choice):
    """
    This function prints out a Tic Tac Toe board on screen, Based on the values present in the position_choice List object.
    :param position_choice: A list object that contains board markings from index 1 - 9.
    :return: Prints a tic tac toe board with values from position_choice input object mapped on to it.
    """
    space, d_space, pipe = ' ', ' ' * 2, '|'
    corner_line = d_space + pipe
    divider = '-' * 17 + '\n'
    blank_line = ((space * 5 + pipe) * 2 + '\n')
    boundary = blank_line + divider + blank_line

    def choice(a, b, c):
        return (d_space + check_for_empty(position_choice[a]) + corner_line) + (
                d_space + check_for_empty(position_choice[b]) + corner_line) + (
                d_space + check_for_empty(position_choice[c]) + d_space) + '\n'

    board = (blank_line + choice(7, 8, 9) + boundary + choice(4, 5, 6) + boundary + choice(1, 2, 3) + blank_line)
    print(board)


def setup_player(player_dict):
    """
    This function accepts a dictionary and returns the same object after having updated it valid with player ids.
    :param player_dict: Dictionary which will be updated
    :rtype Dictionary
    :return: Updated player_dict with valid player ids.
    """
    pl_choice = input("Player 1: What would you like to be, 'X' or 'O': ")
    pl_choice = pl_choice.lower()
    while pl_choice not in ('x','o'):
        pl_choice = input("Player 1: What would you like to be, 'X' or 'O': ")
    else:
        if pl_choice == 'x':
            player_dict['P1'] = 'X'
            player_dict['P2'] = 'O'
        else:
            player_dict['P1'] = 'O'
            player_dict['P2'] = 'X'
    print('Player 1 will be {} and Player 2 will be {}'.format(player_dict['P1'], player_dict['P2']))
    return player_dict


def place_marker(board, marker, position):
    """
    Adds a marker to a board at a certain position.
    :param board: A list object.
    :param marker: Value to be included in the board object.
    :param position: Index in the board list at which marker will be added.
    :return Doesn't return an object, rather updates the board list that is passed.
    """
    board[position] = marker


def win_check(board, mark):
    """
    Return true if mark has won the board else False.
    :param board: List object
    :param mark: mark to be checked for winning combination.
    :return: True if mark has won the board, else false.
    """
    winning_combination = mark * 3

    return ''.join(board[1:4]) == winning_combination or \
           ''.join(board[4:7]) == winning_combination or \
           ''.join(board[7:]) == winning_combination or \
           board[1] + board[4] + board[7] == winning_combination or \
           board[2] + board[5] + board[8] == winning_combination or \
           board[3] + board[6] + board[9] == winning_combination or \
           board[1] + board[5] + board[9] == winning_combination or \
           board[3] + board[5] + board[7] == winning_combination


def space_check(board, position):
    """
    Checks whether index at 'position' is available on 'board'
    :param board: List object which is to be checked.
    :param position: Index on board list to be checked.
    :return: True if position is available else False.
    """
    return board[position] == ''


def full_board_check(board):
    """
    Returns true if no more empty space is available on the board.
    :param board: List object
    :return: Boolean true/false.
    """
    return '' not in board[1:10]


def player_choice(board, player_mark, player):
    """
    Excepts a board, the players id and player's name, validates whether correct move is supplied, depending on which
    either plays the move or prompts the player for correction.
    :param board: List object which keeps the score.
    :param player_mark: 'X" or 'O'
    :param player: P1 or P2
    :return: Calls the place_marker function to update the tic tac toe board.
    """
    choice_index = 0
    while not 0 < choice_index < 10:
        try:
            choice_index = int(input("{} Choose your move (1-9): ".format(player)))
            if not 0 < choice_index < 10:
                raise ValueError
        except ValueError:
            print('Enter a valid option!')
        else:
            while not space_check(board, choice_index):
                print("Spot already occupied! Choose another spot.")
                choice_index = int(input("{} Choose your move (1-9): ".format(player)))
            else:
                place_marker(board, player_mark, choice_index)


def replay():
    """
    Starts fresh game if player chooses to replay else prints a courtesy message.
    """
    decision = input('Do you want to play again? (Y/N): ')
    if decision == 'Y':
        start_game()
    else:
        print('Have a nice day!')


def start_game():
    """
    Orchestrator
    """
    # Clear score board
    score_board = ['#'] + [''] * 9

    player_info = {}
    # Star Game
    game_on = True
    # Welcome Message..
    print('Welcome to Tic Tac Toe!')

    # Player setup
    setup_player(player_info)
    print('Player 1 goes first.\n')
    display_board(score_board)

    # Game Begins
    while game_on:
        # Player 1 Turn
        player_choice(score_board, player_info['P1'], 'P1')
        if win_check(score_board, player_info['P1']):
            display_board(score_board)
            print('Player 1 Wins!')
            game_on = False
            break
        if full_board_check(score_board):
            print('Nobody Wins :-(')
            game_on = False
            break
        display_board(score_board)

        # Player 2 Turn
        player_choice(score_board, player_info['P2'], 'P2')
        if win_check(score_board, player_info['P2']):
            display_board(score_board)
            print('Player Two Wins!')
            game_on = False
            break
        if full_board_check(score_board):
            print('Nobody Wins :-( !)')
            game_on = False
            break
        display_board(score_board)
    replay()

if __name__ == "__main__":
    begin_game = ''
    while begin_game not in ('y', 'n'):
        try:
            begin_game = input('Ready to play (Y/N): ')
            begin_game = begin_game.lower()
            if begin_game.isdigit():
                raise ValueError
        except ValueError:
            print("Choose a valid option!")

    if begin_game == 'y':
        start_game()
    else:
        print('No Worries! Come back when you are ready!')