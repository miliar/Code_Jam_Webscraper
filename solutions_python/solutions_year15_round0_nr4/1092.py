__author__ = 'Nikola Culumovic'

gabriel_wins = [
    "1 1 1",
    "1 1 2",
    "1 1 3",
    "1 1 4",
    "1 2 1",
    "1 2 2",
    "1 2 3",
    "1 2 4",
    "1 3 1",
    "1 3 2",
    "1 3 3",
    "1 3 4",
    "1 4 1",
    "1 4 2",
    "1 4 3",
    "1 4 4",
    "2 1 2",
    "2 1 4",
    "2 2 1",
    "2 2 2",
    "2 2 3",
    "2 2 4",
    "2 3 2",
    "2 3 4",
    "2 4 1",
    "2 4 2",
    "2 4 3",
    "2 4 4",
    "3 2 3",
    "3 3 2",
    "3 3 3",
    "3 3 4",
    "3 4 3",
    "4 3 4",
    "4 4 3",
    "4 4 4"]
max_area = [0, 1, 2, 4, 6, 9, 12]

number_of_cases = int(input())
for i in range(number_of_cases):
    case_input = str(input())
    if case_input in gabriel_wins:
        print("Case #"+str(i+1)+": GABRIEL")
    else:
        print("Case #"+str(i+1)+": RICHARD")