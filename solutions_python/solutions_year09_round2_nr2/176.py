#!/usr/bin/env python
"""
usage: python file.py < X-small/large.in
"""


def main():
    for casenum in range(input()):
        numb = input()
        numb_list = [int(i) for i in str(numb) if i != '0']
        sorted_nl = sorted(numb_list)

        n = 0
        found = False
        while True:
            new_numb = [int(i) for i in str(n) if i != '0']
            if sorted(new_numb) != sorted_nl:
                n += 1
                continue
            if found:
                break
            if n == numb:
                found = True
            n += 1
            

        print 'Case #%d: %d' % (casenum + 1, n)

if __name__ == '__main__':
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass
    main()
