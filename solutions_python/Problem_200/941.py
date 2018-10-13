import sys
def solve(s):
    max_val = 9
    for x in range(len(s)-1, -1, -1):
        d = int(s[x])
        if d > max_val:
            s[x] = str(d-1)
            max_val = d-1
            for i in range(x+1, len(s)):
                s[i] = '9'
        elif d < max_val:
            max_val = d
    start = 0
    while start < len(s) and s[start] == '0':
        start += 1
    s = s[start:]
    return ''.join(s)

t = int(next(sys.stdin))
for test in range(t):
    s = list(next(sys.stdin).strip())
    print ('Case #{}: {}'.format(test+1, solve(s)))
