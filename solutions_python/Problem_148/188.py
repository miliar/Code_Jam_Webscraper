from bisect import bisect
for t in range(int(input())):        
    N, X = map(int, input().split())
    S = list(map(int, input().split()))
    disks = 0
    S = sorted(S)
    while S:
        disks += 1
        if len(S) == 1: break
        m = S[0]
        goal = X - m
        index = bisect(S, goal) - 1
        if index > 0:
            del S[index]
        del S[0]
    print('Case #{}: {}'.format(t+1, disks))
