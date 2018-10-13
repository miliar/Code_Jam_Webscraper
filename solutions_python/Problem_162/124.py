def revdigits(nr):
    return int(str(nr)[::-1])

def precomp(N):
    arr = [0 for i in xrange(0, N+1)]
    arr[1] = 1
    for i in xrange(2,N+1):
        arr[i] = arr[i-1]+1
        if i%10!=0:
            R = revdigits(i)
            if R < i and arr[R] < arr[i]:
                arr[i] = arr[R] + 1
    return arr


def solve(in_name, out_name):
    fin = open(in_name, 'r');
    L = [int(x.strip()) for x in fin.readlines()[1:]]
    fin.close()    
    brute_precomp = precomp(max(L))        
    out = ["Case #" + str(i+1) + ": " + str(brute_precomp[L[i]]) + "\n" for i in xrange(len(L))]
    fout = open(out_name, 'w')
    fout.writelines(out)
    fout.close()
    return

#sys.setrecursionlimit(1010)	
#solve('A-test.in', 'A-test.out')	
#solve('A-small-attempt0.in', 'A-small-attempt0.out')
solve('A-small-attempt0.in', 'A-small-attempt0.out')
