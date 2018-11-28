from collections import defaultdict
patterns = []
canbe = defaultdict(list)

def generateAll(N):
    global patterns
    global canbe
    patterns.append([1, 0, 0])
    for i in range(N):
        last = patterns[-1]
        thisOne = last[:]
        for j in range(3):
            thisOne[j] = last[(j + 2) % 3]
            thisOne[j] += last[j]
        patterns.append(thisOne)

    for i in range(N, 0, -1):
        for j in range(3):
            canbe[patterns[i][j]].append(patterns[i - 1][j])


def generate(R, P, S):
    if R + P + S == 1:
        if R == 1:
            return 'R'
        elif P == 1:
            return 'P'
        else:
            return 'S'
    if R == S:
        piece0 = generate(canbe[R][0], canbe[P][0], canbe[S][1])
        piece1 = generate(canbe[R][1], canbe[P][0], canbe[S][0])
    elif R == P:
        piece0 = generate(canbe[R][0], canbe[P][1], canbe[S][0])
        piece1 = generate(canbe[R][1], canbe[P][0], canbe[S][0])
    else:
        piece0 = generate(canbe[R][0], canbe[P][0], canbe[S][1])
        piece1 = generate(canbe[R][0], canbe[P][1], canbe[S][0])
    if piece0 < piece1:
        return piece0 + piece1
    else:
        return piece1 + piece0

def solve(N, R, P, S):
    pattern = patterns[N]
    if sorted(pattern) != sorted([R, P, S]):
        return 'IMPOSSIBLE'
    return generate(R, P, S)

def main():
    global patterns
    T = input()
    generateAll(12)
    for i in xrange(1, T + 1):
        N, R, P, S = map(int, raw_input().split())
        print 'Case #{0}: {1}'.format(i, solve(N, R, P, S))

if __name__ == '__main__':
    main()
