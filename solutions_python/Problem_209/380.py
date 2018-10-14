from math import pi

input = open('A-small-attempt5.in', 'r')
output = open('A-small-attempt5.out', 'w')
t = int(input.readline().rstrip())
for test in range(t):
    output.write("Case #" + str(test + 1) + ": ")
    n, k = map(int, input.readline().rstrip().split())
    pancs0 = [0] * n
    for i in range(n):
        r, h = map(int, input.readline().rstrip().split())
        pancs0[i] = [2 * pi * r * h, r, pi * r ** 2]
    surf = 0
    for mask in range(2 ** n):
        tmp = list(map(int, bin(mask)[2:]))
        tmp = [0] * (n - len(tmp)) + tmp
        if sum(tmp) == k:
            pancs = []
            for i in range(n):
                if tmp[i]:
                    pancs.append(pancs0[i])
            pancs.sort(reverse = True, key = lambda x: x[1])
            surf_ = pancs[0][0] + pancs[0][2]
            for i in range(1, k):
                surf_ += pancs[i][0]
            surf = max(surf, surf_)
    print(surf, file = output)

input.close()
output.close()