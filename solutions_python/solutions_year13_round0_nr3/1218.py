'''
Created on Apr 13, 2013

@author: akshay
'''

def ckeckFairAndSquare(integer):
    if (str(integer)==str(integer)[::-1]) and (integer**.5)%1==0:
        if str(int((integer**.5)))==str(int((integer**.5)))[::-1]:
            return True
        else:
            return False
    else:
        return False

fp = open("C-small-attempt0.in","r")
list=fp.readlines()
list=[x.strip() for x in list]
list=[x.split() for x in list]
for i in range(len(list)):
    list[i] = [int(x) for x in list[i]]

T=int(list.pop(0)[0])

for i in range(T):
    check=0
    for j in range(list[i][0],list[i][1]+1):
        if ckeckFairAndSquare(j)==True:
            check+=1
    print "Case #%d: %d"%(i+1,check)
