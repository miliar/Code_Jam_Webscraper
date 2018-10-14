from operator import mul
from functools import reduce

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    u = float(input())
    cores = [float(s) for s in input().split(" ")]

    cores.sort(reverse=True)

    s = sum(cores)
    num = len(cores)
    rem = []

    while True:
        avg = s / num
        u_avg = u / num
        t_avg = avg + u_avg

        if cores[0] > t_avg:
            s -= cores[0]
            rem.append(cores[0])
            cores = cores[1:]
            num -= 1
        else:
            break

    prob = reduce(mul, rem, 1)
    prob *= t_avg ** num

    print("Case #{}: {:.6f}".format(i, prob))
