# https://code.google.com/codejam/contest/5304486/dashboard

if __name__ == "__main__":
    filein = open('20171AA.in', 'r')
    fileout = open('20171AA.out', 'w')
    T = int(filein.readline())
    for t in range(T):
        fileout.write('Case #%d: \n' % (t + 1))
        [R, C] = map(int, filein.readline().split())
        cake = []
        for i in range(R):
            cake.append(list(filein.readline().strip()))
        i_start = 0
        for i in range(R):
            j_start = 0
            for j in range(C):
                if cake[i][j] != '?':
                    cake[i][j_start:j] = [cake[i][j] for _ in range(j - j_start)]
                    j_start = j + 1
            if j_start not in (-1, C):
                cake[i][j_start:C] = [cake[i][j_start - 1] for _ in range(j - j_start + 1)]
            if j_start != 0:
                cake[i_start:i] = [cake[i] for _ in range(i - i_start)]
                i_start = i + 1
        cake[i_start:R] = [cake[i_start - 1] for _ in range(i - i_start + 1)]
        fileout.write('\n'.join([''.join(cake[i]) for i in range(R)]) + '\n')

    filein.close()
    fileout.close()
