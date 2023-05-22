import tic_tac_toe


def main():
    """Create the game's board and run its main loop."""
    game = tic_tac_toe.TicTacToeGame()
    board = tic_tac_toe.TicTacToeBoard(game)
    board.mainloop()


if __name__ == "__main__":
    main()
