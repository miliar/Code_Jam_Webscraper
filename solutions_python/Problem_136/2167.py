#!/usr/bin/env python
"""gcj code. """

from sys import stdin


def main():
    x = stdin.readline()
    y = int(x)
    for i in xrange(1, y + 1):
        print "Case #%d: %s" % (i, realmain(i))


def realmain(case):
    l = stdin.readline().strip("\n")
    l = l.split(' ')
    C = float(l[0])
    F = float(l[1])
    X = float(l[2])
#    print C, F, X
    return foo(C, F, X)


def foo(C, F, X):
    tim = 0.0
    rate = 2.0
    balance = 0.0
    tick = 1.0 / rate
    while balance < X:
        remain = X - balance
        if balance >= C:
            inflect = 1.0 * C / F
            optionB = (remain + C) / (rate + F)
            gap = remain / rate
#            print "gaptime: %f, inflect: %f ___ rate:%f diff %f" % (gap, inflect, rate, (X - balance))
#            if gap < inflect:
#                pass
#            else:
            if optionB <= gap:
                balance -= C
                rate += F
                tick = 1.0 / rate

        stride = min(remain, C)
        tgap = stride / rate
        tim += tgap
        balance += stride
        '''
        if remain > 0.999999999999:
            tim += tick
            balance += 1
        else:
            print 'fract %f; tim %f' % (remain, tim)
            tim += tick * remain
            break
        '''

    return "%.8f" % tim


#####################################################

if __name__ == '__main__':
    main()
