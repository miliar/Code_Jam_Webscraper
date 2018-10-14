def tidy(N):
    correction = [int(z) for z in N]
    for y in range(0, len(correction) - 1):
        if(correction[y] > correction[y + 1]):
            correction[y] = correction[y] - 1
            for w in range(y + 1, len(correction)):
                correction[w] = 9
            break
    correction_string = list(map(str, correction))
    NN = "".join(correction_string)
    if(NN != N):
        tidy(NN)
    if(NN == N):
        final.append(NN)

final = []
T = int(input())
for i in range(0, T):
    N = input()
    tidy(N)

for out in range(0, T):
    print("Case #%d: %d" % (out + 1, int(final[out])))
