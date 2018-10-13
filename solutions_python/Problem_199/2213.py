
def flip(lst):
    return ['-' if c == '+' else '+' for c in lst]


def solution(line):
    line, k = line.split()
    line = list(line)
    k = int(k)

    if line == list('+' * len(line)):
        return 0

    n = line.count('-')
    p = line.count('+')

    #if (k % 2) != (n % 2) != (p % 2):
    #    return "IMPOSSIBLE"

    n_flips = 0
    for i in range(len(line)-k+1):
        if line[i] == '-':
            n_flips += 1
            line[i:i+k] = flip(line[i:i+k])

    if line != list('+' * len(line)):
        return "IMPOSSIBLE"

    return n_flips


if __name__ == '__main__':

    import sys

    T = int(sys.stdin.readline())

    for i, line in enumerate(sys.stdin):
        print "Case #{}: {}".format(i+1, solution(line))

