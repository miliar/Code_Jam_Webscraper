IMPOSSIBLE = "IMPOSSIBLE"
CASE_FMT = "Case #{}: {}"
DBG = False


def dbg(mess):
    if DBG:
        print("_ {}".format(mess))


if __name__ == "__main__":
    n = int(input())
    for i in range(1, n + 1):
        line, size = input().split()
        size = int(size)
        state = list(map(lambda x: True if x == "+" else False, line))
        flips = 0
        for j in range(len(state) + 1 - size):
            dbg("{} {}".format(j, state[j:j + size]))
            if not state[j]:
                flips += 1
                state[j:j + size] = map(lambda x: not x, state[j:j + size])
                dbg("\t {}".format(state))
        dbg(state)
        if not all(state):
            flips = IMPOSSIBLE
        print(CASE_FMT.format(i, flips))
