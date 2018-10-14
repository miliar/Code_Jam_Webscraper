inv_map = {'-': '+', '+': '-'}

def inv(s):
    flipped = ''
    for c in s:
        flipped += inv_map[c]
    return flipped

def flip(s, i ,k):
    if (i + k) > (len(s)):
        return (s, 0)
    return (s[:i] + inv(s[i:i+k]) + s[i+k:], 1)

def solve(s, k):
    n = 0
    mc = s.count('-')
    if k == 1 or not mc:
        return mc

    for i in xrange(len(s)):
        if s[i] == '-':
            s, inc = flip(s, i, k)
            n += inc
    if '-' in s:
        return 'IMPOSSIBLE'
    return n


g = open('alarge.out', 'w')

with open('alarge.in', 'r') as f:
    T = f.readline()
    case = 1
    for line in f.readlines():
        s, k = line.split(' ')
        k = int(k)
        r = solve(s, k)
        print 'Case #%s: %s' % (case, r)
        g.write('Case #%s: %s\n' % (case, r))
        case += 1

g.close()