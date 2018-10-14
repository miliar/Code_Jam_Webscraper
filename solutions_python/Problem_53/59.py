
def solve(N, K):
    if (K+1)%(2**N)==0:
        return 'ON'
    else:
        return 'OFF'

fin = open('A-large.in', 'r')
fout = open('out.txt', 'w')
nc = int(fin.readline().rstrip())
for i in range(1,nc+1):
    N, K = [int(s) for s in fin.readline().rstrip().split()]
    fout.write('Case #%d: %s\n'%(i, solve(N, K)))
    
fin.close()
fout.close()
