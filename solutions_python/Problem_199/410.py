import sys

def flip(s):
    return ''.join('+' if e=='-' else '-' for e in s)

def solve(line):
    tmp = line.split()
    s, k = tmp[0], int(tmp[1])
    #if k % 2 != s.count('-') % 2:
    #    return 'IMPOSSIBLE'
    impossible = True
    n = 0
    while True:
        if s.count('+') == len(s):
            return n
        pos = s.find('-')
        if len(s) - pos < k:
            assert impossible
            return 'IMPOSSIBLE'
        s = s[0:pos] + flip(s[pos:pos+k]) + s[pos+k:]
        n += 1
    assert not impossible
    return 1

n = int(input())

for i in range(n):
    solution = solve(input())
    print('Case #%d: %s' % (i+1, solution))
