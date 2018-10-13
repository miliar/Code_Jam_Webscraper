from collections import defaultdict

def check(x):
    x = str(x)
    for i in range(len(x)-1):
        if x[i]>x[i+1]:
            return False
    return True

def conv(x):
    ans = str(x)
    ans = ans[:len(ans)-1]+'9'
    return int(ans)

def ret_ind(x):
    for i in range(len(x)-1):
        if x[i+1]<x[i]:
            return i+1

def make(x):
    x = list(str(x))
    while not check("".join(x)):
        i = ret_ind(x)
        for j in range(i,len(x)):
            x[j]='9'
        x[i-1] = str(int(x[i-1])-1)
        #print x
    return "".join(x)    

t = input()
for i in xrange(t):
    n = input()
    temp = n
    ans = 0
    if check(n):
        ans = n
    else:    
        ans = make(n).lstrip('0')
    print "Case #{}: {}".format(i+1,ans)