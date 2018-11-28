import sys
import math

def chunks(l, n):
    return (l[i:i+n] for i in xrange(0, len(l), n))

if __name__ == '__main__':
    lines = [x.strip() for x in sys.stdin.readlines()]
    lines = [x for x in lines if x]

    for case_num, case in enumerate(lines[1:]):
        low, high = map(int, case.split(' '))

        solutions = 0
        for i in xrange(low, high + 1):
            str_i = str(i)
            if str_i == ''.join(reversed(str_i)):
                sqrt_i = math.sqrt(i)
                if sqrt_i.is_integer():
                    str_sqrt_i = str(int(sqrt_i))
                    if str_sqrt_i == ''.join(reversed(str_sqrt_i)):
                        solutions += 1

        print 'Case #%d: %d' % (case_num + 1, solutions)
