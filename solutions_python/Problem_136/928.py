

import sys


if __name__ == '__main__':
    input = sys.stdin
    T = int(input.readline())
    for t in xrange(T):
        time = 0
        prod = 2.0
        c, f, x = map(float, input.readline().split())
        found = False
        while not found:
            wf = (c / prod) + x / (prod + f)
            wtf = x / prod
         #   print wtf, wf
            if wtf < wf:
                print 'Case #%s: %s' % (t + 1, wtf + time)
                found = True
            else:
                time += c / prod
                prod += f
          #      print "TP", time, prod


