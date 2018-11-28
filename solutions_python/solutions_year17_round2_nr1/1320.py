T = int(input())
for t in range(1, T+1):
    D, N = [int(i) for i in input().split()]
    A = []
    for j in range(N):
        k, s = [int(i) for i in input().split()]
        A.append((D-k)/float(s))
    max_time = max(A)
    print("Case #" + str(t)+ ": " + str(D/max_time))