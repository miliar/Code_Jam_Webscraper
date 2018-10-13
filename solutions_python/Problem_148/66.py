import sys
T = input()
for t in range(T):
    N, M = map(int, raw_input().split())
    files = map(int, raw_input().split())
    cnt = 0

    files.sort()
    while files:
        cur = files.pop()
        cnt += 1
       
        i = len(files) - 1
        for x in reversed(files):
            if x+cur <= M:
                files.pop(i)
                break
            i -= 1
        else:
            continue
    print 'Case #%d:' % (t+1), cnt
    print >>sys.stderr, t
