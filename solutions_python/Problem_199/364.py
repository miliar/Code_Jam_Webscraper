def solve(s, n):
    l = [x == '+' for x in s]
    result = 0
    end = len(s) - n
    start = 0
    while True:
        try:
            start = l.index(False, start)
        except ValueError:
            return result
        if start > end:
            return -1
        for i in range(start, start + n):
            l[i] = not l[i]
        result += 1


t = int(input())
for i in range(t):
    s, n = input().split()
    r = solve(s, int(n))
    print('Case #%d: %s' % (i + 1, 'IMPOSSIBLE' if r == -1 else str(r)))