from scipy.misc.common import comb

ns = [int(x) for x in open("C-small-attempt0.in").readlines()[1:]]

mxn = max(ns)

table = []
for n in range(mxn+1):
    table.append([0] * n)

for n in range(2,mxn+1):
    table[n][1] = 1

for n in range(2,mxn+1):
    for m in range(2,n):
        s = 0
        for j in range (max(1,2*m-n),m):
            s += table[m][j] * comb(n-m-1,m-j-1,1)
            s %= 100003
        table[n][m] = s
    
        #table[n][m] = sum(table[m][max(1,2*m-n):m]) % 100003

for line in table:
    print line

with open("output3.txt","w") as f:
    for i in range(len(ns)):
        f.write("Case #%d: %d\n" % ( i+1, sum(table[ns[i]]) % 100003) )

