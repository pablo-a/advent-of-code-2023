NUMBERS = [str(i) for i in range(10)]


def get_digits(line: str) -> tuple[int, int]:
    for char in line:
        if char in NUMBERS:
            first = int(char)
            break

    for char in line[::-1]:
        if char in NUMBERS:
            last = int(char)
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
