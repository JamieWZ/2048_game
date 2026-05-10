from game_functions import *


def main():
    board = create_board()
    play_game(board)


def play_game(board):
    score = 0
    continue_game = True
    while continue_game:
        print_board(board)
        print("Your score:", score)

        user_input = input("Enter your movement:w/a/s/d ")
        if user_input == "w":
            score += move_up(board)
        elif user_input == "a":
            score += move_left(board)
        elif user_input == "s":
            score += move_down(board)
        elif user_input == "d":
            score += move_right(board)
        else:
            print("Invalid input, please try again")
            continue

        add_new_tile(board)
        clear_screen()

        if is_winner(board):
            print_board(board)
            print("You win!")
            user_choice = input("Would you like to play again? (y/n) ")
            if user_choice == "y":
                return play_game(create_board())
            elif user_choice == "n":
                return

        if is_game_over(board):
            print('Game Over! You lose!')
            user_choice = input("Would you like to play again? (y/n) ")
            if user_choice == "y":
                return play_game(create_board())
            elif user_choice == "n":
                return


if __name__ == '__main__':
    main()

