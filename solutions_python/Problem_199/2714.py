
cases = int(input())

all_cases = []
for i in range(cases):
    test_case = input()
    m, n = test_case.split()
    n = int(n)
    all_cases.append((m, n))





def possible(tup):
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
                m[i] = flip(m[i])
                list_moves[count].append(i)
        else:
            for i in range(first_index, first_index + n):
                m[i] = flip(m[i])
                list_moves[count].append(i)

        if list_moves.count(list_moves[count]) > 1:
            return "IMPOSSIBLE"
        count += 1




def flip(str):
    if str == "-":
        return "+"
    else:
        return "-"

def find_index(m):
    for i in range(len(m)):
        if m[i] == "-":
            return i

    return -1


for i in range(len(all_cases)):
    print("Case #{}: {}".format(i+1, possible(all_cases[i])))