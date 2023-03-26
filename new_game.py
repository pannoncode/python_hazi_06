
from game_setup import GameSetup


def game_chance():
    game_setup = GameSetup()
    valid = False

    while valid is False:
        inp_chance = input(
            "Add meg hányszor szeretnél próbálkozni, hogy eltaláld a számot: ")
        try:
            int(inp_chance)
            print(f"A probálkozásaid száma: {inp_chance}")
            game_setup.set_chance(inp_chance)
            valid = True
            return game_setup.chance
        except:
            print("Nem számot adtál meg!")
            valid = False


def number_range():
    game_setup = GameSetup()
    valid = False
    while valid is False:
        print("Add meg, hogy mettől meddig gondoljon egy számra!")
        from_num = input("Add meg, mettől induljon: ")
        to_num = input("Add meg, hogy meddig: ")
        try:
            int(from_num)
            int(to_num)
            game_setup.set_from_number(from_num)
            game_setup.set_to_number(to_num)
            number = game_setup.random_number()
            return number
        except:
            print("Nem számot adtál meg!")
            valid = False


def new_game():
    num_mach = False
    chance = game_chance()
    counter = 0
    number = number_range()

    while counter < chance:
        inp_numb = input(
            f"Melyik számra gondoltam ({chance - counter} lehetőséged van): ")
        try:
            int(inp_numb)
            if int(inp_numb) == number:
                print(
                    f"!!!ELTALÁLTAD!!! A szám: {number}. Próbálkozásaid száma: {counter + 1}")
                num_mach = True
                counter = chance
            elif int(inp_numb) > number:
                print(f"A gondolt szám kisebb mint a {inp_numb}!")
            elif int(inp_numb) < number:
                print(f"A gondolt szám nagyobb mint a {inp_numb}!")
            counter += 1
        except:
            if inp_numb == "":
                print(
                    "Nem adtál meg semmit! Vigyázz, mert ezzel is csökken az esélyed!")
            else:
                print(
                    "Nem számot adtál meg! Vigyázz, mert ezzel is csökken az esélyed!")
            counter += 1

    if num_mach == False:
        print(f"Vége a játéknak, a gondolt szám: {number}")


new_game()
