import sys
sys.stdin = open('B-large.in')
sys.stdout = open('B-large.out', 'w')

def solve():
    n = int(sys.stdin.readline())
    l = len(str(n))
    digits = map(int,str(n))

    for _i in xrange(l):
        chg = False
        for idx, digit in enumerate(digits):
            if not chg and idx>0 and digit < digits[idx-1]:
                digits[idx-1] -= 1
                chg = True
            if chg:
                digits[idx] = 9

    return int(''.join(map(str, digits)))

t = int(sys.stdin.readline())
for _t in xrange(t):
    print "Case #" + str(_t + 1) + ":", solve()

