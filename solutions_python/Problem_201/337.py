t = int(input())

def update(d, k, inc):
    if k in d:
        d[k]+=inc
    else:
        d[k]=inc

for i in range(t):
    s = input().split(' ')
    n = int(s[0])
    k = int(s[1])

    gaps={n:1}

    while k > 0:
        gap = max(gaps)
        count = gaps[gap]

        if k > count:
            k -= count
            gaps.pop(gap)
            update(gaps, gap//2, count)
            update(gaps, (gap-1)//2, count)
        else:
            y = gap//2
            z = (gap-1)//2
            break

    print("Case #{}: {} {}".format(i+1, y, z))

