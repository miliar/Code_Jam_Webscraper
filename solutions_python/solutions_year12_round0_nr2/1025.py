def main():
    with open('input.txt', 'r') as input, open('output.txt', 'w') as output:
        T = input.readline()
        for i in range(1, int(T)+1):
            L = input.readline().split()
            N = int(L[0])
            S = int(L[1])
            p = int(L[2])
            y = 0
            if p == 0:
                y = N
            else:
                for j in range(3, 3+N):
                    t = int(L[j])
                    if t == 0:
                        continue
                    q, r = divmod(t, 3)
                    if q >= p:
                        y += 1
                    elif q + 1 == p:
                        if r == 0:
                            if S:
                                S -= 1
                            else:
                                continue
                        y += 1
                    elif q + 2 == p:
                        if r == 2 and S:
                            S -= 1
                            y += 1
            output.write('Case #' + str(i) + ': ' + str(y) + '\n');

if __name__ == "__main__":
    main()
