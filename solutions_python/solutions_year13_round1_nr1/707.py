f = file("Bullseyesmall.txt")
text = f.readlines()

cases = int(text[0])

def func(R,T):
    count = R-1
    ans = 0
    a = 1
    while a==1:
        count+=2
        if (2*count-1)<T:
            ans+=1
            T=T-(2*count-1)
        elif (2*count-1)==T:
            ans+=1
            return ans
        elif (2*count-1)>T:
            return ans
        


import math
p = math.pi
count = 0
for i in range(cases):
    count+=1
    RT = map(int,text[count].split())
    R = RT[0]
    T = RT[1]
    dec = func(R,T)
    print 'Case #'+str(i+1)+': '+str(dec)
