nb_cases = int(input())
for ncase in range(nb_cases):
    x = [int(x) for x in input()]
    bye = False
    while not bye:
        bye = True
        for i in range(len(x)-1,0,-1):
            if x[i] < x[i-1]:
                x[i-1] -= 1
                for j in range(i, len(x)):
                    x[j] = 9
                bye = False
                break
    print("Case #{}: {}".format(ncase+1, int(''.join(str(k) for k in x))))