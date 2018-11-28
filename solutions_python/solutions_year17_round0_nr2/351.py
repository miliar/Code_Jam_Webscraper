inputfile = r'B-large.in'
outputfile = r'B-large.out'

def tidy_num(N):
    if len(N) == 1:
        ans = N
    else:
        for i in range(len(N)-1 , 0 , -1):
            if int(N[i-1]) > int(N[i]):
                N = N[:i-1] + str(int(N[i-1])-1) + '9' * (len(N) - i)
        ans = str(int(N))
    return ans

#input
import os
os.chdir(r'C:\codejam\b')
FILENAME = inputfile 
f = open(FILENAME)
lines = f.readlines()
f.close()

#calc
T = int(lines.pop(0)[:-1])
ans = ''
for i in range(T):
    N = lines.pop(0)[:-1]
    ansline = 'Case #' + str(i+1) + ': ' + tidy_num(N)
    ans += ansline + '\n'
    
#output
fout = open(outputfile, 'wt')
print(ans, file = fout)
fout.close()
