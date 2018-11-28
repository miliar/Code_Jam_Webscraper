import sys

def generate_tree(n,A,B,C,D,x0,y0,M):
    X = x0
    Y = y0
    result = []
    result.append((X,Y))
    for i in range(1,n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        result.append((X,Y))
    return result


def good(a,b,c):
    if ((a[0] + b[0] + c[0]) % 3 == 0 and (a[1] + b[1] + c[1]) % 3 == 0):
        return True
    else:
        return False


def solve(trees):
    count = 0
    for i in trees:
        for j in trees:
            if i == j:
                continue
            for k in trees:
                if j == k or i == k:
                    continue
                if good(i,j,k):
                    count += 1
    return count / 6


f = open(sys.argv[1])
C = int(f.readline())
for case in range(C):
    terms = f.readline().split(" ")
    n = int(terms[0])
    A = int(terms[1])
    B = int(terms[2])
    C = int(terms[3])
    D = int(terms[4])
    x0 = int(terms[5])
    y0 = int(terms[6])
    M = int(terms[7])
    
    trees = generate_tree(n,A,B,C,D,x0,y0,M)
    result = solve(trees)
    print "Case #%d: %s" % (case+1, result)

f.close()
