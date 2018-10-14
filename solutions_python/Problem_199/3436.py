ca = int(input())
cases = [input().split() for i in range(ca)]

def poss(tppl):
    m, n = tppl
    n = int(n)
    m = [i for i in m]
    count = 0
    moves = []
    while True:
        first_index = find_index(m)
        if first_index == -1:
            return count
        moves.append([])
        if first_index + n > len(m):
            for i in range(len(m) - n, len(m)):
                m[i] = flip(m[i])
                moves[count].append(i)
        else:
            for i in range(first_index, first_index + n):
                m[i] = flip(m[i])
                moves[count].append(i)

        if moves.count(moves[count]) > 1:
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


for i in range(len(cases)):
    print("Case #{}: {}".format(i+1, poss(cases[i])))