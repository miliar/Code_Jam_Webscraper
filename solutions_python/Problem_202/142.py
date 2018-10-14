def input(fname):
    lines = []
    with open(fname, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def solve(first_line, ans, n):
    opos = -1
    for j, c in enumerate(first_line):
        if c == 'x':
            ans.append(('o', 1, j+1))
            opos = j
        elif c == 'o':
            opos = j
    for j, c in enumerate(first_line):
        if c == '.':
            if opos < 0:
                ans.append(('o', 1, j+1))
                opos = j
            else:
                ans.append(('+', 1, j+1))
    if opos < 0:
        ans.append(('o', 1, n))
        opos = n-1
    tot = n + 1
    j = 0
    for i in range(1, n):
        if j == opos:
            j += 1
        ans.append(('x', i+1, j+1))
        j += 1
    if n > 2 and opos == n-1:
        ans.pop()
        ans.append(('o', n, n-1))
    for i in range(2,n):
        ans.append(('+', n, i))
    if n > 2 and opos == n-1:
        ans.pop()
    return (3*n - 2) if n>1 else 2


def main():
    lines = input('D-small.in')
    l = 1
    tt = 1
    while l < len(lines):
        n, m = map(int, lines[l].split())
        ans = []
        first_line = ['.']*n
        l += 1
        for i in xrange(m):
            tp, i, j = lines[l].split()
            first_line[int(j)-1] = tp
            l+=1
        first_line = ''.join(first_line)
        pts = solve(first_line, ans, n)
        print "Case #{}: {} {}".format(tt, pts, len(ans))
        tt+=1
        for a,b,c in ans:
            print a,b,c


if __name__ == "__main__":
    main()