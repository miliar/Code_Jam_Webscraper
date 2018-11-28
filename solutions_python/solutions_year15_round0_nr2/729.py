opt = dict()
for i in range(1,1000): opt[ tuple([0]*i) ] = 0

def fix(l):
    ret = [ max(0,x-1) for x in l ]
    return ret

def solve(x):
    l = sorted(list(x))
    if tuple(l) in opt: return opt[tuple(l)]
    A = fix(l)
    ans = solve(A)+1
    if l[-1] > 1:
        for i in range(1,l[-1]):
            A = l[:]
            A[-1] = l[-1] - i
            A.append(i)
            A = sorted(A)
            ans = min(ans,solve(A)+1)
    opt[tuple(l)] = ans
    return ans

A = raw_input().rstrip()
B = raw_input().rstrip()

with open(A) as fin:
    T = int(fin.readline().rstrip())
    fout = open(B,'w')
    for t in range(1,T+1):
        fin.readline()
        l = [ int(x) for x in fin.readline().rstrip().split() ]
        fout.write( "Case #" + str(t) + ": " + str(solve(l)) + '\n' )
    fout.close()
    
