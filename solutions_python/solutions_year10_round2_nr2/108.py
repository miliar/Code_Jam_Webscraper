'''
Created on 22/05/2010

Picking Up Chicks

@author: Soloman
'''

def solve(N, K, B, T, X, V):
    pos_at_t = [X[i]+V[i]*T for i in range(N)]
    print(pos_at_t)
    a=0
    pos = N-1
    _pass = 0
    for i in range(N-1, -1, -1):
        if pos_at_t[i]>=B:
            if i==pos:
                pos=pos-1
            else:
                a=a+(pos-i)
                pos=pos-1
            _pass = _pass+1
        if _pass==K:
            return a
    return 'IMPOSSIBLE'

file_dir=''
input_file = file_dir + 'B-large.in'
output_file = file_dir + 'out.txt'

fin=open(input_file, 'r')
fout=open(output_file, 'w')

T=int(fin.readline())
for t in range(1, T+1):
    N, K, B, T = [int(x) for x in fin.readline().split()]
    X = [int(x) for x in fin.readline().split()]
    V = [int(x) for x in fin.readline().split()]
    
    ans = 'Case #%d: %s\n'%(t, solve(N, K, B, T, X, V))
    print(ans)
    fout.write(ans)
fin.close()
fout.close()