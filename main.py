# Copyright 2024 - 2024, Marwin Eising and the terminalGame contributors
import source.game as game

if __name__ == '__main__':
    runner = game.Game("ressources/start.txt")
    runner.load_game()
    runner.start()
    if runner.playerName == "New Player":
        runner.get_player_name()
    else:
        print("Let us continue where we left off, {}".format(runner.get_player_name()))
    runner.save_game()
