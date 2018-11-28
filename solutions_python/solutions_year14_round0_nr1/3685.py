import re

def main():
    T = int(raw_input())
    for case in xrange(1, T+1):
        n = int(raw_input())
        for r in xrange(1, 4+1):
            ints = map(int,raw_input().split())
            if r == n:
                s1 = set(ints)
        n = int(raw_input())
        for r in xrange(1, 4+1):
            ints = map(int,raw_input().split())
            if r == n:
                s2 = set(ints)
        s = s1 & s2
        if len(s) > 1:
            msg = 'Bad magician!'
        elif len(s) < 1:
            msg = 'Volunteer cheated!'
        else:
            msg = list(s)[0]
        print 'Case #%d: %s' % (case, msg)

if __name__ == '__main__':
    main()
