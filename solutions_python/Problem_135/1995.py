import sys
T = int(sys.stdin.readline())

def tcase():
    a = int(sys.stdin.readline())
    ma = [map(int, sys.stdin.readline().split()) for j in xrange(4)]
    b = int(sys.stdin.readline())
    mb = [map(int, sys.stdin.readline().split()) for j in xrange(4)]
    com = set(ma[a-1]) & set(mb[b-1])
    if len(com) == 0:
        print 'Volunteer cheated!'
    elif len(com) == 1:
        print list(com)[0]
    else:
        print 'Bad magician!'

for i in xrange(1, T+1):
    print 'Case #%d:' % i,
    tcase()