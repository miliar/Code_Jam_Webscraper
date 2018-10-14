T = int(input())
format_string = "Case #{0}: {1}"

for i in range(T):
    first_row = int(input())
    possibilities = list()
    rows = list()
    for j in range(4):
        rows.append(input())

    possibilities = rows[first_row - 1]
    possibilities = possibilities.strip().split(" ")
    possibilities = [int(x) for x in possibilities]

    second_row = int(input())
    second_possibilities = list()
    rows = list()
    for j in range(4):
        rows.append(input())

    second_possibilities = rows[second_row - 1]
    second_possibilities = second_possibilities.strip().split(" ")
    second_possibilities = [int(x) for x in second_possibilities]

    final = list()

    for x in possibilities:
        if x in second_possibilities:
            final.append(x)

    if len(final) == 0:
        print(format_string.format(i+1, "Volunteer cheated!"))
    elif len(final) == 1:
        print(format_string.format(i+1, final[0]))
    else:
        print(format_string.format(i+1, "Bad magician!"))
