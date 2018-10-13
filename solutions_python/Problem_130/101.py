
fin = open('/Users/alex/Desktop/codejam3/b/B-large.in', 'r')
fout = open('/Users/alex/Desktop/codejam3/b/B-large.out', 'w')

numcases = int(fin.readline().strip())

# Returns max
def runtourn(n, t):
    if t==1:
        return 0
    if n==1:
        return 1
    if t<= 2**(n-1):
        return 2*runtourn(n-1, t)
    return max( 2*runtourn(n-1, t-2**(n-1))+1, 2*runtourn(n-1, t))

def runtourn2(n, t):
    if t==2**n:
        return 2**n-1
    return 2**n-2-run2(n, 2**n-t)

# tests if k can always win
def run(n, t, k):

    if k>t:
        return False
    if k==0:
        return True
    if t<=2**(n-1):
        return k==0
    if k==1:
        return True
    return run(n-1, t-2**(n-1), (k-1)/2)
    
def run2(n, t):
    def helper(top, bottom):
        if top==bottom:
            return top
        k = (top+bottom+1)/2
        if run(n, t, k):
            return helper(k, bottom)
        return helper(top, k-1)
    return helper(0, 2**n-1)


for case in range(numcases):
    line = fin.readline()
    n, t = line.strip().split(' ')
    n = int(n)
    t = int(t)
    answer = "Case #"+str(case+1)+": "+str(run2(n, t))+ " "+str(runtourn2(n, t))+"\n"
    fout.write(answer)
    print answer

fin.close()
fout.close()
