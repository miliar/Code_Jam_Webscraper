__author__ = 'snv'


# sys.setrecursionlimit(10001)


f = open('A-large.in','r')
g = open('output.txt', 'w')
T = int(f.readline())
for j in range(T):
    cakes, pan = f.readline().split()
    pan = int(pan)
    flips = 0
    wrong_cakes = [cake == '-' for cake in cakes]
    for i_cake in range(len(cakes) - pan + 1):
        if wrong_cakes[i_cake]:
            flips += 1
            for n_cake in range(i_cake, i_cake+pan):
                wrong_cakes[n_cake] = not (wrong_cakes[n_cake])
    all_good = True

    for cake in wrong_cakes[-pan:]:
        if cake:
            all_good = False

    if all_good:
        ans = flips
    else:
        ans = 'IMPOSSIBLE'
    ans_string = 'Case #{0}: {1}\n'.format(j+1, ans)
    print(ans_string)
    g.write(ans_string)
f.close()
g.close()

