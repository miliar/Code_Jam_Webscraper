#!/usr/bin/python2

import sys

def main():

    for n, line in enumerate(open(sys.argv[1])):

        if n == 0:
            continue

        l = line.split()
        l.reverse()

        b = []
        o = []

        for i in xrange(int(l.pop())):
            c = l.pop()
            b.append((c[0:2], c[2]))
        for i in xrange(int(l.pop())):
            c = l.pop()
            o.append(c)

        l.pop() # discard string length
        s = ''
        for c in l.pop():
            # Invoke
            s += c

            # Combine
            for base, combine in b:
                    ss = s[len(s)-2:]
                    if base in ss or base[::-1] in ss:
                        s = s[:-2] + combine

            # Oppose
            for oppose in o:
                if oppose[0] in s and oppose[1] in s:
                    s = ''

        print 'Case #%d: ' % n + '[' + ', '.join([c for c in s]) + ']'

    pass

if __name__ == "__main__":
    main()

