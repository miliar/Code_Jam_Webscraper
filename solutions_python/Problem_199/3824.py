"""
Problem A
T - number of test cases
K - number of pancakes that can be flipped at once
S - row of pancakes [string]: 
        + happy side
        - blank side
"""
HAPPY = '+'
BLANK = '-'

IMPOSSIBLE = 'IMPOSSIBLE'
ZERO = 0


def solve_input_file():
    T = int(input())
    for t in range(1, T + 1):
        S, K = input().split(" ")
        result = get_number_of_flips(list(S), int(K))
        print("Case #{}: {}".format(t, result))


def get_number_of_flips(row: list, flipper_size: int):
    number_of_flips = 0
    current = 0
    process = True
    while process:
        try:
            current = row.index(BLANK, current)
        except ValueError:
            return number_of_flips
        if current + flipper_size > len(row):
            return IMPOSSIBLE
        for i in range(current, current + flipper_size):
            row[i] = flip_single(row[i])
        number_of_flips += 1
    return number_of_flips


def flip_single(side):
    if side == HAPPY:
        return BLANK
    else:
        return HAPPY


if __name__ == "__main__":
    solve_input_file()
