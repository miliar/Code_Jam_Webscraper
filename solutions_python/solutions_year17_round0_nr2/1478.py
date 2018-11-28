# https://code.google.com/codejam/contest/3264486/dashboard#s=p1
if __name__ == "__main__":
    filein = open('2017QB.in', 'r')
    fileout = open('2017QB.out', 'w')
    T = int(filein.readline())
    for t in range(T):
        fileout.write('Case #%d: ' % (t + 1))
        N = filein.readline().strip()
        N_orig = N
        prev_start = 0
        print(N)
        for i in range(1, len(N)):
            if N[i] > N[prev_start]:
                prev_start = i
            elif N[i] < N[prev_start]:
                N = N[:prev_start] + str(int(N[prev_start]) - 1) + '9' * (len(N) - prev_start - 1)
                break
        assert(int(N_orig) >= int(N))
        fileout.write(N.lstrip('0') + '\n')

    filein.close()
    fileout.close()
