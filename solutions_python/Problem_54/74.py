import sys

def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a % b)

c = int(sys.stdin.readline())
for testcase in xrange(1,c+1):
    case = map(int, sys.stdin.readline().split())
    numbers = case[1:]

    cur_gcd = 0
    for n1 in numbers:
        for n2 in numbers:
            if(n1 > n2):
                cur_gcd = gcd(cur_gcd, n1 - n2)

    y = numbers[0] % cur_gcd
    if(y > 0):
        y = cur_gcd - y

    print 'Case #{0}: {1}'.format(testcase, y)
