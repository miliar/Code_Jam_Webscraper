import fileinput
import math

input = fileinput.input()

def maxes(nums):
    nums = list(set(nums))
    f = s = 0
    for num in nums:
        if num > s:
            if num > f:
                f, s = num, f
            else:
                s = num
    return (f, s)

# def divide(f):
#     return [math.floor(f / 2.0), math.ceil(f / 2.0)]

def divide(f, count):
    m = (f, 0)
    for i in range(2, f + 1):
        t = math.ceil(f / float(i)) + (i - 1) * count
        if t < m[0]:
            m = (t, i)
    if m[1] == 0:
        return ([], -1)
    r = []
    for i in range(m[1]):
        r.append(0)
    i = 0
    while f > 0:
        r[i] += 1
        i = (i + 1) % m[1]
        f -= 1
    return (r, m[1] - 1)

def split(cakes, f):
    count = cakes.count(f)
    divided, cost = divide(f, count)
    if cost == -1:
        return ([], -1)
    for c in range(count):
        cakes.remove(f)
        cakes.extend(divided)
    return (cakes, cost * count)

# def split(cakes, f, i):
#     cakes.remove(f)
#     cakes.extend([i, f - i])
#     return cakes

def tick(cakes):
    return map((lambda x: max(0, x - 1)), cakes)

def solve(cakes):
    m = max(cakes)
    if (m == 1):
        return 1
    s, cost = split(cakes[:], m)
    if cost == -1:
        return 1 + solve(tick(cakes))
    return min(1 + solve(tick(cakes)), cost + solve(s))

cases = int(input.readline())
for c in range(cases):
    starters = int(input.readline())
    cakes = map((lambda x: int(x)), input.readline().split())
    print "Case #" + str(c + 1) + ": " + str(solve(cakes))
