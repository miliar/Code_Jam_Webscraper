
def initialize_possible():
    # possible, surprising
    possible = [[0] * 11 for x in xrange(31)]
    surprising = [[0] * 11 for x in xrange(31)]

    
    for i in xrange(11):
        for j in xrange(11):
            for k in xrange(11):
                total = i + j + k
                minv = min([i,j,k])
                maxv = max([i,j,k])
                if maxv > minv + 2:
                    continue
                
                if minv + 1 >= maxv:
                    possible[total][maxv] = 1
                if minv + 2 >= maxv:
                    surprising[total][maxv] = 1

    for i in range(len(possible)):
        v = 0
        for j in xrange(10, -1, -1):
            if possible[i][j]:
                v = 1
            possible[i][j] = v

    for i in range(len(surprising)):
        v = 0
        for j in xrange(10, -1, -1):
            if surprising[i][j]:
                v = 1
            surprising[i][j] = v


    return possible, surprising


def solve(s, p, ns):
    pos, sup = initialize_possible()
    tmp = []
    
    for n in ns:
        tmp.append((pos[n][p], sup[n][p]))
    
    table = [[0 for x in xrange(s+1)] for y in xrange(len(ns) + 1)]



    for i in xrange(len(ns)):
        n = ns[i]
        for j in xrange(s+1):
            table[i+1][j] = table[i][j]        

        if tmp[i][0]:
            for kk in xrange(s+1):
                if table[i+1][kk] > 0 or kk == s:
                    table[i+1][kk] += 1

        if tmp[i][1]:
            for j in xrange(0, s):
                table[i+1][j] = max(table[i+1][j], table[i][j+1]+1)
                
        
    return table[-1][0]
            

def run(inputfile):
    junk = inputfile.readline()
    case = 1
    for line in inputfile:
        xs = line.split()
        N = int(xs[0])
        S = int(xs[1])
        P = int(xs[2])
        ns = map(int, xs[3:])
        
        print "Case #%d: %d" % (case, solve(S, P, ns))
        case += 1


if __name__ == "__main__":
    import sys
    run(open(sys.argv[1]))

