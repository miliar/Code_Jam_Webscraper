import math

def get_l_r_sum(n):
    total = []
    count = []
    c = n
    step = 1

    while c > 0:
        base = pow(2, step-1)
        c = (n - (pow(2, step) - 1)) / base

        odd = 0
        fraction = c % 1
        if fraction > 0:
            odd = base * fraction
            total.append((math.ceil(c), int(odd)))

        total.append((math.floor(c), int(base - odd)))

        step += 1
    return total

def get_answer(n, k):

    lookup = get_l_r_sum(n)
    count = 0
    for pair in lookup:
        if pair[0] < 0:
            continue
        count += pair[1]
        if count >= k:
            b = pair[0] // 2
            a = pair[0] - b
            return a, b
    return 0, 0


t = int(input())
for i in range(1, t + 1):
    n, k = input().split(" ")
    n, k = int(n), int(k)

    max_, min_ = get_answer(n, k)
    print("Case #{}: {} {}".format(i, max_, min_))
