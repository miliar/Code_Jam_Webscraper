import math
def prime(x):
    for factor in range (2, 1000):#int(math.sqrt(x)+1)): #1000 for large
        if x%factor==0:
            return factor
    else:
        return 0
def binary(x):
    x = int(x)
    binaryx = ""
    z=x
    if x==0:
        return 0
    else:
        pass
    y = (math.log(x, 2) // 1) + 1
    while y!=0:
        if z < 2**(y-1):
            binaryx = binaryx + "0"
        else:
            binaryx = binaryx + "1"
            z = z - (2**(y-1))
        y = y-1
    return binaryx
    
'''
with open("A-large2016Q.in") as f:
    a = f.readline()
    for x in range (0, int(a)):
        '''
print("Case #" + str(1) + ":")
b = 32
c = 500
answercount = 0
for j in range (0, 2**(b-2)):
    factorlist = []
    k = binary(j)
    k = str(k)
    while len(k)!=b-2:
         k = "0" + k
    k = "1" + k + "1"
    for l in range (2,11):
        m = 0
        for n in range (0,b):
            m = m + (l**n)*int(k[b-n-1])
        factorlist.append(prime(m))
    factorproduct = 1
    for o in range (0,9):
        factorproduct = factorproduct*factorlist[o]
    if factorproduct == 0:
        pass
    else:
        p = factorlist
        print(k, p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])
        answercount = answercount + 1
        if answercount == c:
            break
        else:
            pass
            
            

        

