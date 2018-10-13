#pan, S= input().split()
#list(map(int, input().split()))
T = int(input())
for uniqueindice in range(T):
    D,N = map(int, input().split())
    time = 0
    for i in range(N):
        K,S = map(int, input().split())
        temps = (D-K) / S
        time = max(time, temps)

    print("Case #{}:".format(uniqueindice+1), end = " ")
    print("{0:.6f}".format(D/time))
