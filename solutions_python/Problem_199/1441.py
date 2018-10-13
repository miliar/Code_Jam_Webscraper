import sys


def flip(line, k, start):
    for i in range(start, start+k):
        line[i] = not line[i]

    return line


def solve(line):
    line = str(line)
    line, k = line.split(" ")
    k = int(k)

    pancakes = [a == '+' for a in line]
    del line

    flips = 0
    for i in range(0, len(pancakes) - k + 1):
        if not pancakes[i]:
            pancakes = flip(pancakes, k, i)
            flips += 1

    print >> sys.stderr, pancakes, k

    done = True
    for c in pancakes:
        if not c:
            done = False

    if done:
        return flips
    else:
        return "IMPOSSIBLE"


if __name__ == "__main__":
    inp = sys.stdin.readlines()
    inp = inp[1:]

    T = len(inp)

    for i, input_line in enumerate(inp):
        ans = solve(input_line)
        ans = "Case #{}: {}".format(i+1, ans)
        print ans
        print >> sys.stderr, ans
