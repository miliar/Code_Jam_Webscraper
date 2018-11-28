def rec(n, k):
    if n == 1:
        return 0, 0
    if n == 2:
        return 1, 0
    if k == 1:
        return n//2, (n-1)//2

    if n % 2 == 0:
        if k % 2 == 0:
            return rec(n//2, k-1)
        return rec((n-1)//2, k-2)
    if k % 2 == 0:
        return rec(n//2, k-1)
    return rec(n//2, k-2)


def solve(n, k):
    if k > (n+1)//2:
        return 0, 0
    if k == 1:
        return n//2, (n-1)//2
    return rec(n, k)


def ans(stalls):
    i = stalls.index(max(stalls))
    left = 0
    j = i-1
    while j >= 0 and stalls[j] == 0:
        j -= 1
        left += 1
    right = 0
    j = i+1
    while j < len(stalls) and stalls[j] == 0:
        j += 1
        right += 1
    return max(left, right), min(left, right)


def sim(n, k):
    stalls = [0 for _ in range(n)]
    x = 1
    while k:
        left = [0 for _ in range(n)]
        count = 0
        for i in range(n):
            left[i] = count
            if stalls[i] != 0:
                count = 0
                left[i] = -1
            else:
                count += 1

        right = [0 for _ in range(n)]
        count = 0
        for i in range(n-1, -1, -1):
            right[i] = count
            if stalls[i] != 0:
                count = 0
                right[i] = -1
            else:
                count += 1

        ind, xx, yy = -1, -1, -1
        for i, (a, b) in enumerate(zip(left, right)):
            low, high = min(a, b), max(a, b)
            if low > xx:
                ind, xx, yy = i, low, high
            if low == xx:
                if high > yy:
                   ind, xx, yy = i, low, high

        stalls[ind] = x
        x += 1
        k -= 1   

    return stalls




if __name__ == "__main__":
    for t in range(int(input())):
        n, k = map(int, input().split())
        a, b = ans(sim(n, k))
        print("Case #{}: {} {}".format(t+1, a, b))
