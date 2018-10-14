from itertools import combinations

global Nr
Nr = 0

def brute(R,C,N):
    global Nr
    Nr += 1
    print Nr
    collection = [(i%R, i//R) for i in xrange(R*C)]        
    buckets = [[False for i in xrange(C+1)] for j in xrange(R+1)]
    bestScore = 4*R*C
    for P in combinations(collection, N):
        score = 0
        for i in xrange(R+1):
            for j in xrange(C+1):
                buckets[i][j] = False
        for x in P:
            buckets[x[0]][x[1]] = True
        for i in xrange(R):
            for j in xrange(C):
                if buckets[i][j]:
                    if buckets[i+1][j]:
                        score += 1
                    if buckets[i][j+1]:
                        score += 1
        if score < bestScore:
            bestScore = score
            if bestScore == 0:
                return bestScore
    return bestScore
        

def solve(in_name, out_name):
    fin = open(in_name, 'r');
    L = [map(int, x.strip().split()) for x in fin.readlines()[1:]]
    fin.close()    
    
    out = ["Case #" + str(i+1) + ": " + str(brute(L[i][0], L[i][1], L[i][2])) + "\n" for i in xrange(len(L))]
    fout = open(out_name, 'w')
    fout.writelines(out)
    fout.close()
    return

#sys.setrecursionlimit(1010)	
#solve('A-test.in', 'A-test.out')	
#solve('A-small-attempt0.in', 'A-small-attempt0.out')
#solve('B-test.in', 'B-test.out')
solve('B-small-attempt0.in', 'B-small-attempt0.out')
