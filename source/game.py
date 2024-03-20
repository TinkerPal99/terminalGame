# Copyright 2024 - 2024, Marwin Eising and the terminalGame contributors
from time import sleep as wait
import json


class Game:

    def __init__(self, start_screen_file):
        """
        The Game is a terminal based game with very rudimentary functions as well as a possibility to save the
        current progress.

        :param start_screen_file: handover of a textfile that shows ascii-art for the game start up
        """
        self.__startupScreen = start_screen_file
        self.__savefile = "ressources/save.json"

        self.playerName = "New Player"

    def start(self):
        """
        prints the start_screen_file in a manner of slight delay per line
        :return: Terminal output
        """
        with open(self.__startupScreen, 'r') as startupFile:
            for line in startupFile:
                print(line, end="")
                wait(0.5)
            print("\n\n\n")

    def get_player_name(self):
        """
        Terminal interaction to ask the player for a new name.
        :return: Terminal output
        """
        playerinput = input("Welcome {} \nWould you like to set a new name? y/n \n".format(str(self.playerName)))

        if playerinput == "y":
            self.playerName = str(input("Please enter your new player name within one line. Any sign is allowed.\n"))
            print("Your playername is now set to {}".format(self.playerName))
        elif playerinput == "n":
            print("Your playername will stay {}".format(self.playerName))
        else:
            "InvalidInput - Please enter either `y` for `yes` or `n` for `no`."
            self.get_player_name()

    def save_game(self):
        """
        Saves the current attributes of the Game as a json-file
        :return: ressources/save.json
        """
        with open(self.__savefile, "w") as savefile:
            json.dump(self.__dict__, savefile)
        print("Game saved")

    def load_game(self):
        """
        Loads the savedata from the json-file
        ToDo: Currently loads the savedata from the file as is, any corruption to the file (added items) will be loaded
        as attributes. !Needs fix

        Excepts none existing save files and corrupted save files.
        :return: loaded game data
        """
        try:
            with open(self.__savefile, "r") as savefile:
                print("SaveFile found and loading ...")
                savedata = json.load(savefile)
                self.__dict__ = savedata
                print("Savefile for player {} loaded ... \n\n".format(self.playerName))
        except FileNotFoundError:
            print("No Save File was found, starting a new game")
        except json.decoder.JSONDecodeError:
            print("Save file is badly corrupted. Starting a new save.")
