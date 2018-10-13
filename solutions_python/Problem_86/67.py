f = open('input.txt', 'r')

T = int(f.readline())

for ttt in xrange(1, T + 1):

    N, L, H = map(int, f.readline().strip().split())

    S = map(int, f.readline().strip().split())

    print 'Case #{}:'.format(ttt),

    fin = False

    for s in xrange(L, H + 1):
        for x in S:
            if s % x and x % s:
                break
        else:
            fin = True
            print s
            break

    if not fin:
        print 'NO'
