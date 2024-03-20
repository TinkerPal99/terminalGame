# Copyright 2024 - 2024, Marwin Eising and the terminalGame contributors
from time import sleep as wait
import json


class Game:

    def __init__(self, start_screen_file):
        """
        The Game is a terminal based game with very rudimentary functions as well as a possibility to save the
        current progress.
        :param: start_screen_file: handover of a textfile that shows ascii-art for the game start up
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
        playerinput = self.get_player_choice("Welcome {} \nWould you like to set a new name? y/n \n"
                                             .format(str(self.playerName)),
                                             "string"
                                             )

        if playerinput == "y":
            self.playerName = str(input("Please enter your new player name within one line. Any sign is allowed.\n"))
            print("Your playername is now set to {}".format(self.playerName))
        elif playerinput == "n":
            print("Your playername will stay {}".format(self.playerName))
        else:
            "InvalidInput - Please enter either `y` for `yes` or `n` for `no`."
            self.get_player_name()

    def get_player_choice(self, text, return_type):
        """
        a handler for player input to normalize input and handle wrong input

        :param text: text given when asking for input
        :param return_type: expected type
        :return:normalized player input
        """
        player_input = input(text)

        if return_type == "numerical":
            try:
                player_input = int(player_input)
            except ValueError:
                raise InvalidPlayerInput(type_request=return_type, playerinput=player_input)

        elif return_type == "string":
            player_input = str(player_input)

        elif return_type == "boolean":
            if player_input == "y" or player_input == "yes":
                player_input = True
            elif player_input == "n" or player_input == "no":
                player_input = False
            else:
                raise InvalidPlayerInput(type_request=return_type, playerinput=player_input)

        return player_input

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


class InvalidPlayerInput(Exception):
    """Raised when the player enters bullshit."""

    def __init__(self, type_request, playerinput):
        """

        :param type_request: expected type of the input
        :param playerinput: the entered data by the player
        """
        super().__init__("The player entered some bullshit data. \n  input: {input} \n  requested data type: {type}"
                            .format(
                                input=str(type(playerinput)) + ":" + str(playerinput),
                                type=type_request
                            )
                        )


if __name__ == "__main__":
    test = Game("ressources/start.txt")
    test.get_player_choice("test", "numerical")
