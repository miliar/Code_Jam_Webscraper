from functools import reduce
from operator import xor

def solve(C):
    if reduce(xor, C)==0:
        C.remove(min(C))
        return sum(C)
    else:
        return 'NO' 

            

input_file = 'C-large.in'
output_file = 'result.dat'
fin=open(input_file , 'r')
fout=open(output_file, 'w')

T=int(fin.readline())
for t in range(1, T+1):
    fin.readline()
    C = [int(x) for x in fin.readline().split()]
    ans = 'Case #%d: %s\n'%(t, solve(C))
    print(ans)
    fout.write(ans)
fin.close()
fout.close()