import sys


def parse(instrm):
    state, size = instrm.readline().split()
    return state, int(size)


def solve(case):
    state, size = case
    state = [int(c == "+") for c in state]
    last_start = len(state) - size
    n_moves = 0
    for i in range(last_start + 1):
        if state[i] == 1:
            continue
        n_moves += 1
        for j in range(i, i + size):
            state[j] = 1 - state[j]

    start_check = max(0, last_start + 1)
    for i in range(start_check, len(state)):
        if state[i] == 0:
            return "IMPOSSIBLE"
    return n_moves


if __name__ == "__main__":
    with open(sys.argv[1]) as instrm:
        n = int(instrm.readline())
        for i in range(n):
            case = parse(instrm)
            ans = solve(case)
            print("Case #{}: {}".format(i+1, ans))
