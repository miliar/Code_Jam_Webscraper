import string

def gcd(a,b):
    while b: a,b = b, a%b
    return a

fin = open('b.in', 'r')
fout = open('b.out', 'w')

t = int(fin.readline())

for tc in range(1,t+1):
    fout.write('Case #' + str(tc) + ': ');
    tok = string.split(fin.readline())
    n = int(tok[0])
    d =[]
    for i in range(1,n+1):
        d.append(int(tok[i]))
    d.sort()
    res = d[1]-d[0]
    for i in range(2,n):
        res = gcd(res,d[2]-d[1])
    fout.write(str( (res-d[0]%res)%res ) + '\n')
fin.close()
fout.close()