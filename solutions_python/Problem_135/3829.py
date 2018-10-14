def read_row():
    index = int(input())
    rows = []

    for i in range(4):
        rows.append(list(map(int, input().split(" "))))

    return rows[index - 1]

def do_case():
    row1, row2 = list(map(set, [read_row(), read_row()]))

    intersect = row1 & row2
    size = len(intersect)

    if size == 0:
        print("Volunteer cheated!")
    elif size > 1:
        print("Bad magician!")
    else:
        print(list(intersect)[0])

test_cases = int(input())

for i in range(test_cases):
    print("case #{}: ".format(i + 1), end="")
    do_case()
