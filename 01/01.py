import re

NUMBERS = [str(i) for i in range(10)]
LETTERS_NUMBER = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

NUMBER = r"|".join(LETTERS_NUMBER)
NUMBER_REGEX = rf"^{NUMBER}"


def match_digit_written_in_letter(line: str):
    match = re.match(NUMBER_REGEX, line)
    if match:
        return LETTERS_NUMBER[match.group()]
    return None


def get_digits(line: str) -> tuple[int, int]:
    for index, char in enumerate(line):
        if char in NUMBERS:
            first = int(char)
            break
        if match := match_digit_written_in_letter(line[index:]):
            first = match
            break

    for index in range(len(line) - 1, -1, -1):
        char = line[index]
        if char in NUMBERS:
            last = int(char)
            break
        if match := match_digit_written_in_letter(line[index:]):
            last = match
            break
    return first, last


def main():
    sum = 0

    with open("./input.txt", "r") as f:
        for line in f:
            digit_1, digit_2 = get_digits(line)
            sum += int(f"{digit_1}{digit_2}")

    print(sum)


if __name__ == "__main__":
    main()
