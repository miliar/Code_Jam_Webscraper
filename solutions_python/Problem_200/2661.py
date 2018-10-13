def solve(n):
    data = map(int, str(n))
    i = 0
    decremented = False
    while True:
        try:
            a, b = data[i], data[i+1]
            if a > b or not b:
                data[i] = a - 1 if not decremented else 9
                data[i + 1] = 9
                decremented = True
            i += 1
        except IndexError:
            break
    r = int(''.join(map(str, data)).lstrip('0'))
    if int(''.join(sorted(str(r)))) != r:
        return solve(r)
    return r

def _solve(n):
    if len(str(n)) == 1:
        return n
    if int(''.join(sorted(str(n)))) == n:
        return n
    n -= 1
    while True:
        if int(''.join(sorted(str(n)))) == n:
            return n
        n -= 1
    return n

g = open('blarge.out', 'w')

with open('blarge.in', 'r') as f:
    T = f.readline()
    case = 1
    for line in f.readlines():
        n = int(line)
        r = solve(n)
        print 'Case #%s: %s' % (case, r)
        g.write('Case #%s: %s\n' % (case, r))
        case += 1


g.close()