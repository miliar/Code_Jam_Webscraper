import sys

def main():
    infile, outfile = sys.argv[1:3]
    with open(infile, 'r') as inp:
      with open(outfile, 'w') as out:
        T = int(inp.readline())
        for case in range(1, T+1):
            N = int(inp.readline())
            Naomi = [float(i) for i in inp.readline().split()]
            Ken = [float(i) for i in inp.readline().split()]
            Naomi.sort()
            Ken.sort()
            out.write('Case #{}: '.format(case))
            out.write('{} {}\n'.format(find_dwar(N, Naomi, Ken), 
                                       find_war(N, Naomi, Ken)))


def find_war(N, Naomi, Ken):
    indexKen = 0
    kScore = nScore = 0
    for bNaomi in Naomi:
        while Ken[indexKen] < bNaomi:
            indexKen += 1
            if indexKen == N:
               break
        if indexKen == N:
            break
        kScore += 1
        indexKen += 1
        if indexKen == N:
            break
    nScore = N-kScore
    return nScore

def find_dwar(N, Naomi, Ken):
    return N-find_war(N, Ken, Naomi)

if __name__ == '__main__':
    main()
