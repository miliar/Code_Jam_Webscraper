import sys

def tidy(N):
    for i in range(1,len(N)):
        if N[i] < N[i-1]:
            for j in range(i, 0, -1):
                if N[j] < N[j-1]:
                    N[j] = '9'
                    N[j-1] = str(int(N[j-1])-1)
            for j in range(i+1,len(N)):
                N[j] = '9'
    for i in range(len(N)):
        if i >= len(N):
            break
        if N[i] == '0':
            N.pop(i)
                
    return ''.join(N)

inf = open(sys.argv[1])
inp = inf.read().split('\n')
inf.close()

T = int(inp.pop(0))
outf = open('output.txt','w')
for i in range(T):
    outf.write('Case #{0}: {1}\n'.format(i+1, tidy(list(inp.pop(0)))))

outf.close()
