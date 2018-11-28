DEBUG = False
HAPPY = 1
BLANK = -1

def genlist(S):
    l = []
    for s in S:
        if s == '+':
            l.append(HAPPY)
        else:
            l.append(BLANK)
    return l


def printd(s):
    if DEBUG:
        print(s)


def solve(S, K):
    pancakes = genlist(S)
    l = len(pancakes)
    i = 0
    times = 0
    while True:
        printd("{}: {}".format(i, pancakes))
        if i > l - K:
            done = True
            for j in range(i, l):
                if pancakes[j] == BLANK:
                    done = False
                    return "IMPOSSIBLE"
            break
        if pancakes[i] == HAPPY:
            i += 1
            continue
        else:
            for j in range(i, i + K):
                if pancakes[j] == BLANK:
                    pancakes[j] = HAPPY
                else:
                    pancakes[j] = BLANK
            times += 1
            i += 1
    return times


def main():
    n = int(input())
    for i in range(1, n + 1):
        S, K = [str(s) for s in input().split(" ")]
        out = solve(S, int(K))
        print("Case #{}: {}".format(i, out))

if __name__ == "__main__":
    main()
