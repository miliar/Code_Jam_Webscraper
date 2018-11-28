import numpy
t = int(input())
results = []
for _ in range(t):
    n, k = input().split(" ")
    n = int(n)
    k = int(k)

    a = [n]
    last = k-1
    for i, _ in enumerate(range(k)):
        z = a[0]-1
        del a[0]
        if z == 0:
            if i == last:
                a += [0, 0]
        elif z == 1:
            if i == last:
                a += [1, 0]
            else:
                a.append(1)
        else:
            q, remainder = divmod(z, 2)
            if remainder == 0:
                a += [q, q]
            else:
                a += [q+1, q]
    results.append(a[-2:])

for i in range(t):
    print("Case #{}: {} {}".format(i+1, results[i][0], results[i][1]))
