import math

f = open("in.txt", "r")
fout = open("out.txt", "w")


t = int(f.readline())
for i in range(1, t+1):
    a, b = [int(x) for x in f.readline().split('/')]
    res = 0

    while b % 2 == 0:
        b /= 2
        res += 1

    if a % b == 0:
        a = a / b
        if a % 2 > 0:
            a = math.ceil(a/2)
        while a > 1:
            a /= 2
            res -= 1
    else:
        fout.write("Case #{:d}: impossible\n".format(i))
        continue

    fout.write("Case #{:d}: {:d}\n".format(i, res))