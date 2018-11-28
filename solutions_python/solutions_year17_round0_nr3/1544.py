def cal(S, K):
    max = 0
    min = 0

    if S >= K:
        if (K != 0 and ((K & (K - 1)) == 0)):
            factor = K
            repeat = 0
            for i in range(K, S+1):
                if repeat < factor:

                    repeat += 1
                else:
                    repeat = 1
                    if max == min:
                        max += 1

                    else:
                        min += 1

            return (max, min)

        else:
            # odd
            #start from k - k then count to stall same way but first need to figure out largest power of 2
            X = K
            while(not(X != 0 and ((X & (X - 1)) == 0))):
                X -= 1

            factor = X
            repeat = 0
            for i in range(K, S + 1):
                if repeat < factor:

                    repeat += 1
                else:
                    repeat = 1
                    if max == min:
                        max += 1

                    else:
                        min += 1

            return (max, min)

    else:
        return max,min

def main():
    f = open('C-small-2-attempt0.in', 'r')
    w = open('out.txt', 'w')
    i = 0
    for line in f:
        if i:
            line.strip()
            x = line.split(' ')
            ans = cal(int(x[0]), int(x[1]))
            res = "Case #" + str(i) + ": " + str(ans[0]) + " " + str(ans[1])
            w.write(res + '\n')
        i += 1
    f.close()
    w.close()


main()