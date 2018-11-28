import sys

def process_input(openfile):
    #openfile = open(filename, 'r')
    T = int(openfile.readline()[:-1])
    tests = []
    for j in range(T):
        NK = openfile.readline()
        N, K = [int(s) for s in NK.split(' ')]
        board = []
        for i in range(N):
            row_st = openfile.readline()[:-1]
            row = list(row_st)
            board.append(row)
        tests.append([N, K, board])
    return tests


def largest(j, i, M, N, grid, vals):
    k = 1
    m = min(M-j, N-i)
    ch = grid[j][i]
    verbose = False
    #if (j, i) == (0, 1):
    #    verbose = True
    if verbose:
        print j, i, m, ch 
    for s in range(1, m):
        if verbose:
            print "s = %s"%s
        for t in range(j, j+s+1):
            if verbose:
                print t, i+s, grid[t][i+s], ch
            if grid[t][i+s] == ch or vals[t][i+s] > 1:
                return k
            ch = grid[t][i+s]
        for t in range(i+s-1, i-1, -1):
            if verbose:
                print j+s, t, grid[j+s][t], ch
            if grid[j+s][t] == ch or vals[j+s][t] > 1:
                return k
            ch = grid[j+s][t]
        k += 1
        ch = grid[j][i+s]
    return k


if __name__ == '__main__':
    ### PROGRAM CCCCCCCCCC
    #openfile = open('C.in', 'r')
    # hex 2 bin dict
    hex2bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
               '4': '0100', '5': '0101', '6': '0110', '7': '0111',
               '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
               'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    openfile = sys.stdin
    ET = int(openfile.readline()[:-1])
    for T in range(1, ET+1):
        # read test data
        MN = openfile.readline()
        M, N = [int(s) for s in MN.split(' ')]
        grid = []
        for j in range(M):
            row_hex = openfile.readline()[:-1]
            row = []
            for let in row_hex:
                row = row + [c for c in hex2bin[let]]
            grid.append(row)
        #for j in range(M):
        #    print grid[j]
        vals = [[1 for i in range(N)] for j in range(M)]
        #for j in range(M):
        #    print vals[j]
        size_dict = {}
        while True:
            kmax = 1
            jmax = 0
            imax = 0
            for j in range(M):
                for i in range(N):
                    if vals[j][i] == 1:
                        k = largest(j, i, M, N, grid, vals)
                        if k > kmax:
                            kmax = k
                            jmax = j
                            imax = i
            if kmax == 1:
                break
            for s in range(jmax, jmax+kmax):
                for t in range(imax, imax+kmax):
                    vals[s][t] = kmax
            if size_dict.has_key(kmax):
                size_dict[kmax] += 1
            else:
                size_dict[kmax] = 1

        #for j in range(M):
        #    print vals[j]

        size_dict[1] = 0
        for j in range(M):
            for i in range(N):
                if vals[j][i] == 1:
                    size_dict[1] += 1
        #print size_dict

        sizes = sorted(size_dict.keys())
        sizes.reverse()
        if size_dict[1] == 0:
            sizes.remove(1)
        print 'Case #%s: %s' %(T, len(sizes))
        for s in sizes:
            print "%s %s"%(s, size_dict[s])
    openfile.close()
