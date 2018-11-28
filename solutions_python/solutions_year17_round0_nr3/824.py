from math import log2

def stalls(n, k):
    if k == 1:
        return  ((n - 1) // 2, n // 2)
    ready = 1
    if (n - 1) % 2 == 0:
        small = 2
        large = 0
    else:
        small = 1
        large = 1
    worse = (n - 1) // 2
    while True:
        ready += small + large
        if ready >= k:
            if k <= ready - small:
                return (worse // 2, (worse + 1) // 2)
            else:
                return ((worse - 1) // 2, worse // 2)

        if (worse - 1) % 2 == 0:
            small = small * 2 + large
        else:
            large = large * 2 + small
        worse = (worse - 1) // 2

if __name__ == "__main__":
    with open("input") as fi,\
            open("output", "w") as fo:
        t = int(fi.readline())
        for i in range(1, t + 1):
            n, k = map(int, fi.readline().split())
            s = stalls(n, k)
            r, l = s[1], s[0]
            fo.write("Case #{}: {} {}\n".format(i, r, l))
            #print("Case #{}: {}  {}\n".format(i, r, l))
