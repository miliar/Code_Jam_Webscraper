import numpy as np

fin = open('A-small-attempt2.in')
fout = open('out-small.txt', 'w')

def isqrt(x):
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

T = int(fin.readline().rstrip('\n'))
for iter in range(1,T+1,1):
	pars = np.array(fin.readline().rstrip('\n').split(), dtype=int)
	r = pars[0]
	t = pars[1]
	# print (-(2*r+1) + isqrt(pow(2*r+1,2) + 8*t))/4
	k = int((-(2*r-1) + np.sqrt(pow(2*r-1,2) + 8*t))/4)
	# print k
	fout.write('Case #%d: ' %iter + '%d\n' %k)
	
fin.close()
fout.close()