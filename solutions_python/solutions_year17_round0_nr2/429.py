def isSorted(s):
    if len(s) <= 1:
        return True
    for i in range(1, len(s)):
        if s[i-1] > s[i]:
            return i
    return True

def naiveSolve(line):
    n = int(line)
    res = 0
    for e in range(n, 0, -1):
        s = str(e)
        pos = isSorted(s)
        if pos is True:
            return s
    assert False

def solve(line):
    n = int(line)
    res = 0
    while n>=1:
        s = str(n)
        pos = isSorted(s)
        if pos is True:
            return s
        exp = len(s)-1-pos
        n = n - n % (10 ** (exp+1)) - 1
    assert False

n = int(input())
for i in range(n):
    s = input()
    solution = solve(s)
    #assert solution == naiveSolve(s)
    print('Case #%d: %s' % (i+1, solution))
