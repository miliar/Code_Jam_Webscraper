from __future__ import print_function


def solve():
    file_name = "a"
    file = open(file_name + ".out", "w")
    for i, test_case in enumerate(test_cases(file_name + ".in")):
        rows = []
        for question in test_case:
            row = question[0]
            rows.append(set(question[1][row - 1]))

        line = "Case #{0}: ".format(i + 1)
        intersect = rows[0] & rows[1]
        if len(intersect) > 1:
            line += "Bad magician!"
        elif len(intersect) < 1:
            line += "Volunteer cheated!"
        else:
            line += str(list(intersect)[0])
        record(line, file)


def test_cases(file_name):
    file = open(file_name, "r")
    num_test_cases = int(file.readline())
    results = []
    for __ in range(num_test_cases):
        choice = int(file.readline())
        cards = card_grid(file)
        first = choice, cards

        choice = int(file.readline())
        cards = card_grid(file)
        second = choice, cards

        results.append([first, second])
    return results


def card_grid(file):
    rows = []
    dimension = 4
    for __ in range(dimension):
        cards_cols = file.readline().split()
        row = []
        for col in range(dimension):
            row.append(int(cards_cols[col]))
        rows.append(row)
    return rows


def record(string, file):
    print(string)
    file.write(string + "\n")


solve()