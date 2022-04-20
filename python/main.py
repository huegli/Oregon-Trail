import random
import builtins
import keyboard
import time


def setup():
    # set up the variables to be used in game
    game_variables = {
        # Identification of variables in the program
        # amount spent on animals
        "animals": 0,
        # amount spent on ammunition
        "ammunition": 0,
        # amount spent on clothing
        "clothing": 0,
        # flag for insufficient clothing in cold weather
        "insufficient_clothing": False,
        # counter in generating events
        "event_counter": 0,
        # turn number for setting date
        "game_turn": 0,
        # choice of shooting expertise level
        "shooting_expert_level": 0,
        # choice of eating
        "eating_choice": 0,
        # amount spent on food
        "food": 0,
        # flag for clearing south pass
        "south_pass_flag": False,
        # flag for injury
        "injury": False,
        # flag for blizzard
        "blizzard": False,
        # total mileage whole trip
        "mileage": 0,
        # amount spent on miscellaneous supplies
        "supplies": 0,
        # total mileage up through previous turn
        "turn_mileage": 0,
        # flag for clearing south pass in setting mileage
        "South_Pass_Mileage_Flag": False,
        # flag for illness
        "illness": False,
        # cash in your wallet
        "cash": 700,
        # flag for fort option
        "fort_flag": False
    }
    return game_variables


def shooting():
    print("You pull your gun, aim, and pull the trigger")
    start_time = time.time()
    seconds = 15
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time > seconds:
            print("Pop")
            my_score = 5
            break
        if keyboard.is_pressed(" "):
            if elapsed_time < 1:
                print("Wham!")
                my_score = 1
            elif elapsed_time < 2:
                print("POW!")
                my_score = 2
            elif elapsed_time < 4:
                print("Blam!")
                my_score = 3
            else:
                print("Bang")
                my_score = 4
            break
    return my_score


def illness(game_variables):
    if random.randint(1, 100) < 10 + 35 * (game_variables["eating_choice"] - 1):
        print("Wild Illness - Medicine Used.")
        game_variables["mileage"] = game_variables["mileage"] - 5
        game_variables["supplies"] = game_variables["supplies"] - 2
    elif random.randint(1, 100) < 100 - (40 / 4 ** (game_variables["eating_choice"] - 1)):
        print("Bad Illness - Medicine Used.")
        game_variables["mileage"] = game_variables["mileage"] - 5
        game_variables["supplies"] = game_variables["supplies"] - 5
    else:
        print("Serious Illness - You must stop for Medical Attention.")
        game_variables["illness"] = False
        game_variables["supplies"] = game_variables["supplies"] - 10

    # I'm sorry, but you don't have any more supplies
    if game_variables["supplies"] < 10:
        dying("no_supplies")

    # There was a blizzard so let's return to it...
    if game_variables["blizzard"] == 1:
        return game_variables

    return game_variables
