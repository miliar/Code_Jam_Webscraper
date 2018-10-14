t = int(input())


def piss(n, k):
#    print("##\t", n, k)
    if n == 2 and k == 1:
        return [1, 0]
    elif n == k:
        return [0, 0]
    else:
        if k == 1:
            return [n // 2, (n - 1) // 2]
        elif n % 2 == 1:
            return piss((n - 1) / 2, k // 2)
        else:
            if k%2==1:
                return piss(n/2-1, (k-1)/2)
            else:
                return piss(n/2, k/2)

for c in range(1, t + 1):
    n, k = [int(item) for item in input().split()]
    y, z = piss(n, k)
    print("Case #%d: %d %d" % (c, y, z))
