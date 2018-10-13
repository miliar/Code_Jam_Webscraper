from __future__ import absolute_import, division, print_function

NO = 'IMPOSSIBLE'

def solve(n, r, y, b ):
    result = ""
    last = ''
    if r > y + b:
        return NO
    elif y > r + b:
        return NO
    elif b > r+y:
        return NO

    if max(b, y, r) == r:
        first = 'R'
    elif max(b, y, r) == y:
        first = 'Y'
    else:
        first = 'B'

    while r+b+y > 0:

        if last == 'R':
            most = max(y, b)
        elif last == 'Y':
            most = max(r, b)
        elif last == 'B':
            most = max(y, r)
        else:
            most = max(b, y, r)

        if most == r and not(first != 'R' and (r == b or r == y)) and last != 'R':
            result += 'R'
            r -= 1
            last = 'R'
        elif most == y and not(first != 'Y' and (y == b or r == y)) and last != 'Y':
            result += 'Y'
            y -= 1
            last = 'Y'
        elif most == b and last != 'B':
            result += 'B'
            b -= 1
            last = 'B'
        else:
            if most == r and last != 'R':
                result += 'R'
                r -= 1
                last = 'R'
            elif most == y and last != 'Y':
                result += 'Y'
                y -= 1
                last = 'Y'
            elif most == b and last != 'B':
                result += 'B'
                b -= 1
                last = 'B'
            else:
                return NO
    return result



with open('B-small-attempt1.in') as f:
#with open('sample.in') as f:
    T = int(f.readline())

    for puzzle_count in range(T):
        n,r,o,y,g,b,v = map(int, f.readline().strip().split(' '))

        ans = solve(n, r, y ,b)

        print('Case #%s: %s' % (str(puzzle_count + 1), ans))

