T = int(input())

for x in range(T):
    smax, people = input().split()
    smax = int(smax)

    standing = 0
    plusone  = 0

    for (k, guy) in enumerate(people):
        while standing < k and standing < smax:
            standing += 1
            plusone  += 1

        standing += int(guy)

    print("Case #{0}: {1}".format(x + 1, plusone))
