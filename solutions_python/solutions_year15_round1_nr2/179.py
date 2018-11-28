def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a / gcd(a, b) * b


def f(g, nums):
    if g < 0:
        return 0
    t = 0
    for x in nums:
        t += g / x + 1
    return t


def valids(left, nums):
    val = []
    for i, x in enumerate(nums):
        if left % x == 0:
            val.append(i + 1)
    return val


def ans(nums, n):
    l = 1
    for x in nums:
        l = lcm(x, l)

    rep = sum((l / x) for x in nums)
    n -= 1
    n %= rep
    n += 1

    left, right = 0, l

    while right - left > 1:
        mid = (right + left) >> 1
        fmid = f(mid, nums)
        if fmid > n:
            right = mid
        else:
            left = mid

    fleft = f(left, nums)

    while f(left, nums) == fleft:
        left -= 1
    left += 1

    # print '>>>>>>>>>>', n, left, fleft
    if fleft == n:
        fprev = f(left - 1, nums)
        return valids(left, nums)[n - fprev - 1]
    elif fleft > n:
        fprev = f(left - 1, nums)
        return valids(left, nums)[n - fprev - 1]
    else:
        fprev = fleft
        while f(left, nums) == fleft:
            left += 1
        return valids(left, nums)[n - fprev - 1]
    return left


def debug(nums, N):
    g, l = nums[0], 1
    for x in nums:
        g = gcd(x, g)
        l = lcm(x, l)

    h = []
    for x in nums:
        h.append(l / x)

    rep = sum(h)
    N -= 1
    N %= rep

    # print l
    if l > 1000:
        return

    n2 = []
    for i, x in enumerate(nums):
        for y in range(0, l, x):
            n2.append((y, i))
    n2.sort()
    # print n2
    m = {}
    for i, (a, b) in enumerate(n2):
        m[i] = b
    # print sorted(m.items())
    # print m[N]

    ss = {}
    for i, x in enumerate(nums):
        ss[(i, x)] = []
    for a, b in m.items():
        ss[(b, nums[b])].append(a)
    for a, b in ss.items():
        print a, b
    print


def parts(_type=int):
    return map(_type, raw_input().split())

T = int(raw_input())

for z in range(T):
    B, N = parts(int)
    nums = parts(int)

    # debug(nums, N)
    print 'Case #{}: {}'.format(z+1, ans(nums, N))
