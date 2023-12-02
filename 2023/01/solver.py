import aocd
import re

aocd_input = aocd.get_data(day=1, year=2023)


def solve_first(lines: list[str] | None = None) -> int:
    """
    The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

    For example:

    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet

    In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

    Consider your entire calibration document. What is the sum of all of the calibration values?
    """
    if not lines:
        lines = aocd_input.splitlines()

    sum = 0
    for line in lines:
        # Find the first and last digit
        nums = re.findall(r"\d+", line)
        d1, d2 = nums[0], nums[-1]
        if len(d1) > 1:
            d1 = d1[0]
        if len(d2) > 1:
            d2 = d2[-1]

        digits = str(d1 + d2)
        sum += int(digits)
    return sum


def solve_second(lines: list[str] | None = None) -> int:
    """
    Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

    Equipped with this new information, you now need to find the real first and last digit on each line. For example:

    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen

    In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
    """
    other_valid_digits = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    if not lines:
        lines = aocd_input.splitlines()

    sum = 0
    for line in lines:
        # Potentially replace other valid digits with numbers
        replacements = []
        for digit_word, digit in other_valid_digits.items():
            if digit_word in line:
                # Track replacements so we can replace them later with the index
                index = line.find(digit_word)
                replacements.append({"digit": (digit_word, digit), "idx": index})

        if replacements:
            # Replace the left most digit first
            replacements = sorted(replacements, key=lambda item: item["idx"])
            for r in replacements:
                line = line.replace(r["digit"][0], str(r["digit"][1]))

        # Find the first and last digit
        nums = re.findall(r"\d+", line)
        d1, d2 = nums[0], nums[-1]
        if len(d1) > 1:
            d1 = d1[0]
        if len(d2) > 1:
            d2 = d2[-1]

        digits = str(d1 + d2)
        sum += int(digits)
    return sum

def test():
    # Test part 1
    p1_lines = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
    p1_result = solve_first(lines=p1_lines)
    assert p1_result == 142, p1_result

    # Test part 2
    p2_lines = [
        "two1nine", "eightwothree", "abcone2threexyz", "xtwone3four",
        "4nineeightseven2", "zoneight234", "7pqrstsixteen",
    ]
    p2_result = solve_second(lines=p2_lines)
    assert p2_result == 281, p2_result


if __name__ == "__main__":
    test()

    first = solve_first()
    second = solve_second()

    print(f"First: {first}")
    print(f"Second: {second}")
