def some(tup):
    m, n = tup
    m = [i for i in m]
    count = 0
    list_moves = []
    while True:
        first_index = find_index(m)
        if first_index == -1:
            return count
        list_moves.append([])
        if first_index + n > len(m):
            for i in range(len(m) - n, len(m)):
                m[i] = flip_pancakes(m[i])
                list_moves[count].append(i)
        else:
            for i in range(first_index, first_index + n):
                m[i] = flip_pancakes(m[i])
                list_moves[count].append(i)

        if list_moves.count(list_moves[count]) > 1:
            return "IMPOSSIBLE"
        count += 1


def flip_pancakes(str):
    if str == "-":
        return "+"
    else:
        return "-"


def find_index(m):
    for i in range(len(m)):
        if m[i] == "-":
            return i
    return -1

cases = int(input())
input_cases = []
for i in range(cases):
    test_case = input()
    m, n = test_case.split()
    n = int(n)
    input_cases.append((m, n))

for i in range(len(input_cases)):
    print("Case #{}: {}".format(i+1, some(input_cases[i])))