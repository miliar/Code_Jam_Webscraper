inputfile = r'C-large.in'
outputfile = r'C-large.out'

def lrspace(n):
    if n % 2: #n : odd
        Ls = (n-1)//2
        Rs = (n-1)//2
    else: #n : even
        Ls = n//2 - 1
        Rs = n//2
    return [Ls, Rs]

def get_kc(K):
    i = 2
    table = [1]
    while True:
        add = 2**i - 1
        if add >= K:
            break
        table.append(add)
        i += 1
    return table[-1]

def space(N, K):
    Kc = get_kc(K)
    a, b = divmod((N - Kc),(Kc + 1))
    if K-Kc == 0:
        if b == 0:
            Ls = a
            Rs = a
        else:
            Ls = a
            Rs = a+1
    else:
        if b >= K-Kc:
            Ls, Rs = lrspace(a+1)
        else:
            Ls, Rs = lrspace(a)
    return [Ls, Rs]

#input
import os
os.chdir(r'C:\codejam\c')
FILENAME = inputfile 
f = open(FILENAME)
lines = f.readlines()
f.close()

#calc
T = int(lines.pop(0)[:-1])
ans = ''    
for i in range(T):
    N, K = map(int, lines.pop(0)[:-1].split())
    Ls, Rs = space(N,K)
    y = max(Ls, Rs)
    z = min(Ls, Rs)
    ansline = 'Case #' + str(i+1) + ': ' + str(y) + ' ' + str(z)
    ans += ansline + '\n'
    
#output
fout = open(outputfile, 'wt')
print(ans, file = fout)
fout.close()
