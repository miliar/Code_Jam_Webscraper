'''
Created on Apr 10, 2015

@author: TigerZhao
'''
t = input()
def canFit(r,c,a,b):
    if a*b >r*c:
        return False
    if (a>c and b >c) or (a >r and b >r):
        return False
    return True
def solve(x,r,c):
    if x >7 or (x>r and x >c) :
        return "RICHARD"
    if x>=3:
        a = x**0.5
        a +=1
        a=int(a)
        if not canFit(r,c,a,a):
            return "RICHARD"
        
        
    area = r*c 
    if area % x !=0:
        return "RICHARD"
    return "GABRIEL"
    
for w in range(t):
    te= raw_input().strip().split()
    x = int(te[0])
    r = int(te[1])
    c = int(te[2])
    
    print "Case #{0}: {1}".format(w+1,solve(x,r,c))