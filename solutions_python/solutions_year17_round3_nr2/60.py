def solve():
    ac,aj = [int(v) for v in input().split()]
    c = []
    j = []
    for i in range(ac):
        ci,di = [int(v) for v in input().split()]
        c.append([ci,di])
    for i in range(aj):
        ji,ki = [int(v) for v in input().split()]
        j.append([ji,ki])
    arr = []
    for p in (c):
        arr.append([p[0],p[1],0])
    for p in (j):
        arr.append([p[0],p[1],1])
    arr = sorted(arr, key=lambda p: p[0])
    lc = []
    lj = []
    tot = 0
    for i in range(-1,ac+aj-1):
        if arr[i][2] == arr[i+1][2]:
            if arr[i][2] == 0:
                lj.append((arr[i+1][0]-arr[i][1]) % (24*60))
            else:
                lc.append((arr[i+1][0]-arr[i][1]) % (24*60))
        else:
            tot += 1
    tc = 720
    tj = 720
    for a in c:
        tj -= (a[1]-a[0])
    for a in j:
        tc -= (a[1]-a[0])
    lc = sorted(lc)
    lj = sorted(lj)
    cnt = 0
    for i in lc:
        cnt += i
        if cnt <= tc:
            tot -= 2
        else:
            break
    cnt = 0
    for i in lj:
        cnt += i
        if cnt <= tj:
            tot -= 2
        else:
            break
    tot += 2*len(lc)
    tot += 2*len(lj)
    return tot


T = int(input())
for t in range(1, T + 1):
    print('Case #%d: %d' % (t,solve()))


