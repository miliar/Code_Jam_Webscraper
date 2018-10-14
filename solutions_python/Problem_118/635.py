from __future__ import print_function
import math
import sys
import random

def err(*msgs, **argv):
    print(*msgs, file=sys.stderr, **argv)

def gen2():
    f = open('generated2.txt', 'w')
    err(10000, file=f)
    for i in range(1000):
        A = random.randint(1, 10 ** 14)
        B = random.randint(1, 10 ** 14)
        err(A, B, file=f)
def gen():
    f = open('generated.txt', 'w')
    err(1000, file=f)
    for i in range(1000):
        A = random.randint(1, 10 ** 100)
        B = random.randint(1, 10 ** 100)
        err(A, B, file=f)

def solveLarge(A, B):
    count = 0
    if B <= 1000:
         return solveCase(A, B)
    if A <= 9:
        count = solveCase(A, 9)
        A = 10
    minimal = int(math.ceil(math.sqrt(A)))
    total_digits = len(str(minimal))

    num = '1' + '0' * (total_digits - 1)
    sq = int(num) ** 2
    while sq <= B:
        if int(num) >= minimal and str(num) == str(num)[::-1] and str(sq) == str(sq)[::-1]:
            count += 1
        num = add1(num)
        #sq = int(num + num[::-1]) ** 2
        sq = num ** 2

    return count


def add1(base3):
    base3 = int(base3)
    num = list(str(base3 + 1))
    for i in reversed(range(len(num))):
        if int(num[i]) > 2:
            num[i] = '0'
            if i > 0:
                num[i-1] = str(1 + int(num[i-1]))
            else:
                num = ['1'] + num
    return int(''.join(num))


def solveCase(A, B):
    count = 0
    x = int(math.ceil(math.sqrt(A)))
    while x <= int(math.sqrt(B)):
        square = x ** 2
        rev_x = str(int(str(x)[::-1]))
        rev_sq = str(int(str(square)[::-1]))
        if str(x) == rev_x and str(square) == rev_sq:
            count += 1
        x += 1
    return count

def solveAll(s):
    it = iter(s.split('\n'))
    T = int(it.next())
    for i in range(T):
        A, B = map(int, it.next().split(' '))
        count = solveLarge(A, B)
        # Add the additional last vines with l=0
        yield('Case #%s: %s' % (i + 1, count))

def test():
    #err(solveCase(1,4))
    #err(solveCase(10,120))
    #err(solveCase(1, 10**12))
    #err(solveLarge(1, 10**12))
    err(solveCase(1, 121))
    err(solveLarge(1, 121))
    #err('\n'.join(solveAll(open('C-small-attempt0.in').read())))
if __name__ == '__main__':
    if not sys.argv[1:]:
        test()
        sys.exit(1)
    #err(solveLarge(5155650068634954336540166688416587628065756588121980449099459709315645565419978760056495902406838400,
    #    9627873290151915186858501571446148561850602580418387950183777469009051357493555951176200330826142547))
    fn = sys.argv[1]
    print('\n'.join(solveAll(open(fn).read())))
