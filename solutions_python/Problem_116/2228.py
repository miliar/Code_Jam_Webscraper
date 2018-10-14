# -*- coding: utf-8 -*-


def open_files():
    f = open('input.txt', 'r')
    g = open('output.txt', 'w')
    return f, g


def determine_ended(test_case):
    for element in test_case:
        if '.' in element:
            return False
    return True


def check_lines(test_case):
    for line in test_case:
        if (line.count('X') == 4) or ((line.count('X') == 3) and (line.count('T') == 1 )):
            return 'X won'
        if (line.count('O') == 4) or ((line.count('O') == 3) and (line.count('T') == 1)):
            return 'O won'
    return None


def check_columns(test_case):
    reversed_test_case = []
    for column_index in range(4):
        reversed_test_case.append([])
        for line_index in range(4):
            reversed_test_case[column_index].append(test_case[line_index][column_index])
    return check_lines(reversed_test_case)

def check_diagonals(test_case):
    diag1, diag2 = [], []
    for index in range(4):
        diag1.append(test_case[index][index])
        diag2.append(test_case[index][3 - index])
    return check_lines([diag1, diag2])


def determine_winner(test_case):
    if check_lines(test_case):
        return check_lines(test_case)
    if check_columns(test_case):
        return check_columns(test_case)
    if check_diagonals(test_case):
        return check_diagonals(test_case)
    return None


def determine_game_state(test_case):
    if determine_winner(test_case):
        return determine_winner(test_case)
    else:
        if determine_ended(test_case):
            return "Draw"
        else:
            return "Game has not completed"


f, g = open_files()

number_of_test_cases = int(f.readline())

for index in range(number_of_test_cases):
    test_case = []
    for line_index in range(4):
        line = f.readline()
        test_case.append([])
        for symbol_index in range(4):
            test_case[line_index].append(line[symbol_index])

    f.readline()
    print "Case #" + str(index + 1) + ": " + determine_game_state(test_case)
    g.write("Case #" + str(index + 1) + ": " + determine_game_state(test_case) + '\n')
