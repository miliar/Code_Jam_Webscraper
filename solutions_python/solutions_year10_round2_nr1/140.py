'''
Created on 23/05/2010


@author: Soloman
'''

def solve(N, M):
    _N=set()
    for n in N:
        path = [l for l in n.split('/') if l is not '']
        for i in range(1, len(path)+1):
            _N.add('/'.join(path[:i]))
            
    _M=set()
    for m in M:
        path = [l for l in m.split('/') if l is not '']
        for i in range(1, len(path)+1):
            _M.add('/'.join(path[:i]))
            
    _D = _M.difference(_N)
    return len(_D)

file_dir=''
input_file = file_dir + 'A-large.in'
output_file = file_dir + 'out.txt'

fin=open(input_file, 'r')
fout=open(output_file, 'w')

T=int(fin.readline())
for t in range(1, T+1):
    n, m = [int(x) for x in fin.readline().split()]
    N, M = [], []
    for i in range(n):
        N.append(fin.readline().strip())
    for i in range(m):
        M.append(fin.readline().strip())
        
    ans = 'Case #%d: %d\n'%(t, solve(N, M))
    print(ans)
    fout.write(ans)
fin.close()
fout.close()