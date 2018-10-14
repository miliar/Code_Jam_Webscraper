import fileinput
import pprint

i = []
for line in fileinput.input():
    i.append(line)

test_cases = int(i.pop(0))
cases = []
while test_cases:
    a = int(i.pop(0))

    grid = [[int(d) for d in i.pop(0).strip().split(" ")],
            [int(d) for d in i.pop(0).strip().split(" ")],
            [int(d) for d in i.pop(0).strip().split(" ")],
            [int(d) for d in i.pop(0).strip().split(" ")]]

    b = int(i.pop(0))

    grid_rotated = [[int(d) for d in i.pop(0).strip().split(" ")],
                    [int(d) for d in i.pop(0).strip().split(" ")],
                    [int(d) for d in i.pop(0).strip().split(" ")],
                    [int(d) for d in i.pop(0).strip().split(" ")]]

    test_cases -= 1

    cases.append([a,b,grid,grid_rotated])

def magic_trick(a,b,grid,grid_rotated, case_number):
    possibilities = set(grid[a-1])
    second_possibilities = set(grid_rotated[b-1])

    card = list(possibilities.intersection(second_possibilities))

    # print "Cards:", card

    if len(card) == 1:
        return "Case #%i: %i" % (case_number, card[0])
    elif len(card) > 1:
        return "Case #%i: Bad magician!" % case_number
    elif not card:
        return "Case #%i: Volunteer cheated!" % case_number

case_number = 1
for case in cases:
    a,b,grid,grid_rotated = case

    # pprint.pprint(case)

    print magic_trick(a,b,grid,grid_rotated, case_number)
    case_number += 1