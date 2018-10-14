def solve(ix):
    R0 = int(raw_input().strip())
    M0 = [map(int, raw_input().strip().split()) for _ in range(4)]

    R1 = int(raw_input().strip())
    M1 = [map(int, raw_input().strip().split()) for _ in range(4)]

    intersect = list(set(M0[R0-1]) & set(M1[R1-1])) 

    if len(intersect) == 1:
        ans = intersect[0]
    elif len(intersect) > 1:
        ans = "Bad magician!"
    else:
        ans = "Volunteer cheated!"     

    print 'Case #%d: %s' % (ix, ans)   

N = int(raw_input())
for ix in range(N):
    solve(ix+1)
