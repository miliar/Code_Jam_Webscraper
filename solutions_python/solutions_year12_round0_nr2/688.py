T = int(raw_input())
for i in xrange(T):
    total = 0
    s = map(int,raw_input().split())
    N = s[0]
    S = s[1]
    p = s[2]
    t = s[3:]
    for j in t:
        if j % 3 == 0:
            triplet = [j/3,j/3,j/3]
        elif j % 3 == 1:
            triplet = [j/3,j/3,j/3+1]
        elif j % 3 == 2:
            triplet = [j/3,j/3+1,j/3+1]
        if max(triplet) >= p:
            total += 1
        elif S > 0 and sum(triplet) >= 2:
            if (j%3) in [0,2] and max(triplet)+1 >= p:
                total += 1
                S -= 1
    print 'Case #%d: %d' % (i+1,total)
