t = int(raw_input().strip())


def mycmp(a, b):
    if a[1] > b[1]:
        return -1
    elif a[1] == b[1]:
        if a[0] > b[0]:
            return 1
        else:
            return -1
    else:
        return 1


for i in range(1, t+1):
    n, k = list(map(int, raw_input().strip().split()))
    arr = []
    for j in range(1, n+1):
        di, si = list(map(int, raw_input().strip().split()))
        si = 2*di*si
        di = di*di
        arr.append((di, si))
    arr.sort()
    x = -1
    for ij in range(n-1, k-2, -1):
        ar = arr[0:ij]
        y = arr[ij][0]+arr[ij][1]
        ar.sort(mycmp)
        for ijk in range(0, k-1):
            y += ar[ijk][1]
        if x < y:
            x = y
    x *= 3141592653589793
    x = str(x)
    x = x[0:-15]+"."+x[-15:]
    print("Case #"+str(i)+": "+x)
