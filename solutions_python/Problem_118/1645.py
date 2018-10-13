from math import sqrt, ceil
from time import time

def pal(n):
    t = n
    r = 0
    while t:
        r = r*10 + t%10
        t /= 10
    return r == n       

def pals(a,b):
    return 4
    
def qualc(a,b):
    s = int(ceil(sqrt(a)))
    t = int(sqrt(b))
    r = 0
    
    for i in range(s,t+1):
        if pal(i) and pal(i**2):
            r += 1
            #print a,b,i,i**2
    return r
    
start = time()
f = open('C-large-1.in')
lines = f.readlines()
w = open('C-large-1.out','w')

s = list(filter(lambda x: pal(x) and pal(x**2), xrange(10**7+1)))

def qualc2(a,b):
    return sum(1 for i in s if sqrt(a)<=i<=sqrt(b))
    
for i in range(len(lines)-1):
    words = lines[i+1].strip().split(' ')
    nums = map(int,words)
    #print qualc2(nums[0],nums[1])
    w.write('Case #%s: %s\n' % (str(i+1), str(qualc2(int(words[0]), int(words[-1])))))
    
    
f.close()
w.close()
print time()-start