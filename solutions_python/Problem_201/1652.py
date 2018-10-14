t = int(input())
for i in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]
    vdict = {n:1}
    keys = [n]
    while m > 1:
        x = max(keys)
        if x % 2 == 0:
            if x/2 - 1 in vdict:
                vdict[x/2-1] += 1
            else:
                vdict[x/2-1] = 1
            if x/2 - 1 not in keys:
                keys.append(x/2-1)
            if x/2 in vdict:
                vdict[x/2] += 1
            else:
                vdict[x/2] = 1
            if x/2 not in keys:
                keys.append(x/2)
            if vdict[x] == 1:
                vdict.pop(x)
                keys.remove(x)
            else:
                vdict[x] -= 1
            m -= 1
        else:
            if (x-1)/2 in vdict:
                vdict[(x-1)/2] += 2
            else:
                vdict[(x-1)/2] = 2
            if (x-1)/2 not in keys:
                keys.append((x-1)/2)
            if vdict[x] == 1:
                vdict.pop(x)
                keys.remove(x)
            else:
                vdict[x] -= 1
            m -= 1
    final = max(keys)
    if final % 2 == 0:
        maxi = int(final/2)
        mini = int(final/2 - 1)
    else:
        maxi = int((final - 1)/2)
        mini = int((final - 1)/2)
    print("Case #{}: {} {}".format(i, maxi, mini))
