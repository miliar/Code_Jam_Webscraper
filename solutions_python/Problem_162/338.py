import sys
T = int(sys.stdin.readline())


def main():
    for case in range(1, T + 1):
        res = solve(case)
        sys.stdout.write("Case #{}: {}\n".format(case, res))


def solve(case):
    n = int(sys.stdin.readline())
    bests = [None] * (n + 1)
    bests[1] = 1
    depth = 2
    queue = [1]

    if n == 1:
        return bests[1]

    while True:
        nextqueue = []

        for index in range(0, len(queue)):
            i = queue[index]

            flipped = int(str(i)[::-1])

            if flipped > i and flipped <= n:
                if flipped == n:
                    return depth

                if bests[flipped] is None:
                    bests[flipped] = depth
                    nextqueue.append(flipped)

            if i + 1 == n:
                return depth

            if bests[i + 1] is None:
                bests[i + 1] = depth
                nextqueue.append(i + 1)

        depth += 1
        queue = nextqueue

main()
