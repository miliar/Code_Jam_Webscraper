from collections import deque

def input(fname):
    lines = []
    with open(fname, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

def shouldflip(flip, sign):
    return (flip, sign) in ((1, '+'), (0, '-'))

def solve(line):
    p, k = line.split()
    k = int(k)
    ans = 0
    d = deque()
    flip = 0
    l = len(p)
    for i, c in enumerate(p):
        if d and d[0] == i:
            flip = 1 - flip
            d.popleft()
        if shouldflip(flip, c):
            if i+k > l:
                return 'IMPOSSIBLE'
            ans += 1
            flip = 1 - flip
            d.append(i+k)
    return ans


def main():
    lines = input('A-large.in')
    for c, line in enumerate(lines[1:]):
        print "Case #{}: {}".format(c+1, solve(line))

if __name__ == "__main__":
    main()