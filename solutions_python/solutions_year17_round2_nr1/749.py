N = int(input())

for i in range(N):
    D,H_N = map(int,input().split())
    min_ds = D
    min_sp = 0
    times = []
    for j in range(H_N):
        ds,sp = map(int,input().split())
        times.append([ds,sp,(D-ds)/sp])

    times.sort(key=lambda x:x[0])
    m = max(times, key=(lambda x:x[2]))
    print('Case #'+str(i+1)+': '+'{:.6f}'.format(D/m[2]))
