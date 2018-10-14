import math


for c in range(int(input())):
    n1 = [int(n) for n in input().split()]
    d = n1[0]
    ho = n1[1]
    max = 0
    for h in range(ho):
        n2 = [int(n) for n in input().split()]
        p = n2[0]
        s = n2[1]
        time = (d-p)/s
        if (time > max):
            max = time

    print("Case #%d: %s" % (c+1, d/max))

# if isPow2(c1):
#     print('Case #{0}: {1}'.format(c+1, int(math.log2(c1))))
# else:
#     print('Case #{0}: IMPOSSIBLE'.format(c+1))

