import sys

T = int(sys.stdin.readline())

for i in xrange(T):
        sys.stdout.write('Case #%d: ' % (i+1))
        a = int(sys.stdin.readline())
        s = None
        for j in xrange(4):
                tmp = [int(x) for x in sys.stdin.readline().split()]
                if j+1 == a:
                        s = set(tmp)
        b = int(sys.stdin.readline())
        for j in xrange(4):
                tmp = [int(x) for x in sys.stdin.readline().split()]
                if j+1 == b:
                        s = s & set(tmp)
                        if len(s) == 0:
                                print 'Volunteer cheated!'
                        elif len(s) == 1:
                                print list(s)[0]
                        else:
                                print 'Bad magician!'

