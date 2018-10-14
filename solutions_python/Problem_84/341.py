#!/usr/bin/python2

import sys

def main():

    f  = open(sys.argv[1], 'r')

    TC = int(f.readline())

    for tc in xrange(TC):

        l = f.readline().split()
        R = int(l[0])
        C = int(l[1])

        T = []

        for r in xrange(R):
            s = f.readline().strip()
            l = []
            for c in xrange(C):
                l.append(s[c])
            T.append(l)

        possible = True
        for r in xrange(R-1):
            for c in xrange(C-1):

                if T[r][c] is '.':
                    continue

                if T[r][c] is '#' and T[r][c+1] is '#' and T[r+1][c] is '#' and T[r+1][c+1] is '#':
                    T[r][c] = '/'
                    T[r][c+1] = '\\'
                    T[r+1][c] = '\\'
                    T[r+1][c+1] = '/'

            if not possible:
                break

        s = ''
        for t in T:
            s += ''.join(t)

        print 'Case #%d:' % (tc + 1)
        if '#' in s:
            print 'Impossible'
        else:
            for t in T:
                print ''.join(t)

    f.close()


if __name__ == "__main__":
    main()

