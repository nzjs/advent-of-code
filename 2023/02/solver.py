import aocd
import re

aocd_input = aocd.get_data(day=2, year=2023)

CUBE_COLOURS = ["red", "green", "blue"]


def solve_first(conditions: dict[str], lines: list[str] | None = None) -> int:
    """
    For example, the record of a few games might look like this:

    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

    In game 1, three sets of cubes are revealed from the bag (and then put back again).
    The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes,
    and 6 blue cubes; the third set is only 2 green cubes.

    The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

    In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration.
    However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly,
    game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the
    games that would have been possible, you get 8.

    Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes,
    and 14 blue cubes. What is the sum of the IDs of those games?
    """
    meets_conditions: dict[str] = {}

    if not lines:
        lines = aocd_input.splitlines()

    total = 0
    for line in lines:
        # Find the game id and results
        game_id = line.split(":")[0].strip().split(" ")[1]
        game = line.split(":")[1].strip()

        # Split the reveals by semi-colon
        elf_reveals = game.split(";")
        reveals_passed = True
        for reveal in elf_reveals:
            # Split the cubes by comma
            cubes = reveal.strip().split(",")
            cubes_passed = True
            for cube in cubes:
                # Split the cube into the number and colour
                num, colour = cube.strip().split(" ")
                if colour in CUBE_COLOURS:
                    # Check if the number of cubes matches the conditions
                    if int(num) > conditions[colour]:
                        cubes_passed = False
                        break

            if not cubes_passed:
                reveals_passed = False
                break

        if reveals_passed:
            # Add the game id to the total
            meets_conditions[game_id] = True
            total += int(game_id)

    return total


def test():
    # Test part 1
    p1_lines = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
    p1_conditions = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    p1_result = solve_first(conditions=p1_conditions, lines=p1_lines)
    assert p1_result == 8, p1_result


if __name__ == "__main__":
    test()

    conditions = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    first = solve_first(conditions=conditions)

    print(f"First: {first}")
