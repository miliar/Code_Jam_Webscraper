from sys import stdin

last = None
r, ry, y, yb, b, br = 0, 0, 0, 0, 0, 0

def put_b(result):
    global b, ry, last
    if b > ry:
        result.append('B')
        b -= 1
    while ry:
        result.append('OB')
        b -= 1
        ry -= 1
    last = 'B'

def put_r(result):
    global r, yb, last
    if r > yb:
        result.append('R')
        r -= 1
    while yb:
        result.append('GR')
        r -= 1
        yb -= 1
    last = 'R'

def put_y(result):
    global y, br, last
    if y > br:
        result.append('Y')
        y -= 1
    while br:
        result.append('VY')
        y -= 1
        br -= 1
    last = 'Y'

def ok(a, b):
    if a == 'R':
        return b in 'YBG'
    if a == 'Y':
        return b in 'RBV'
    if a == 'B':
        return b in 'RYO'
    if a == 'O':
        return 'B'
    if a == 'G':
        return 'R'
    if a == 'V':
        return 'Y'
    assert False

def verify(solution):
    assert (all(ok(solution[i], solution[i+1]) for i in xrange(len(solution) - 1))
            and solution[0] != solution[-1])

def main():
    t = int(stdin.readline().strip())
    for k in xrange(1, t+1):
        global last, r, ry, y, yb, b, br
        n, r, ry, y, yb, b, br = (int(s) for s in stdin.readline().strip().split(' '))
        # print "Trying {} {} {} {} {} {} {}".format(n, r, ry, y, yb, b, br)
        if ((ry == 0 or ry < b or (ry == b and ry + b == n)) and
            (yb == 0 or yb < r or (yb == r and yb + r == n)) and
            (br == 0 or br < y or (br == y and br + y == n))):
            bb = b - ry
            rr = r - yb
            yy = y - br
            if bb <= rr + yy and rr <= yy + bb  and yy <= bb + rr:
                result = []
                last = 'B' if b < min(r, y) else ('R' if r < y else 'Y')
                while b or r or y:
                    # print "_ {} {} {}".format(b, r, y)
                    if last == 'B':
                        if y > r:
                            put_y(result)
                        else:
                            put_r(result)                                
                    elif last == 'R':
                        if b > y:
                            put_b(result)
                        else:
                            put_y(result)
                    elif last == 'Y':
                        if r > b:
                            put_r(result)
                        else:
                            put_b(result)
                if result[0] == result[-1]:
                    tmp = result[-2]
                    result[-2] = result[-1]
                    result[-1] = tmp
                solution = ''.join(result)
                verify(solution)
                print "Case #{}: {}".format(k, solution)
            else:
                print "Case #{}: IMPOSSIBLE".format(k)
        else:
            print "Case #{}: IMPOSSIBLE".format(k)

main()
