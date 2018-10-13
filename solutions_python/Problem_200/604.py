import numpy as np
infile = open('in.txt')
outfile = open('out.txt','w')
T = int(infile.readline())
def convert(D):
    a = np.zeros([1, 22])
    l = 0
    while (D>0):
        a[0, l] = D % 10
        l += 1
        D//=10
    return a, l

def check(a, l):
    for i in range(l-1):
        if (a[0, i]<a[0, i+1]):
            return False
    return True

for cases in range(T):
    N = int(infile.readline())
    n = N
    s = ''
    while True:
        (a,l) = convert(n)
        if check(a, l) == True:
            break
        n -= (n % 10 + 1)
        n //= 10
        s += '9'

    if (n == 0):
        ansString = "Case #"+str(cases+1)+": "+s+'\n'
        outfile.write(ansString)
    else:
        ansString = "Case #"+str(cases+1)+": "+str(n)+s+'\n'
        outfile.write(ansString)
infile.close()
outfile.close()