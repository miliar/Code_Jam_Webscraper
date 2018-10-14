
sigmacache = {}

def calculate(C,F,X,n):
    C = float(C)
    F = float(F)
    X = float(X)
    n = int(n)
#     sigma(C/(2+iF))
    sigma = 0
    for i in range(n):
        if(n-2 in sigmacache):
            i=n-1
            sigma = sigmacache[i-1]
        sigma += (C/(2+i*F))
        sigmacache[i] = sigma
    return (sigma + (X/(2+n*F)) )

def solvecase(C,F,X):
    sigmacache.clear()
    cur = calculate(C,F,X,0)
    for i in range(1,10000):
        tmp = calculate(C,F,X,i)
        if tmp < cur:
            cur = tmp
        else:
            break
    else:
        print("n>10000!!")
    return cur

def solve():
    with open(r'd:\B-small-attempt0.in','r') as infile,open(r'd:\Boutput.out','w') as outfile:
        numofcase = int(infile.readline().strip())
        for i in range(numofcase):
            C,F,X = infile.readline().strip().split()
            ans = solvecase(C,F,X)
            outfile.write('Case #%d: %0.7f\n' % (i+1,ans))
solve()
            