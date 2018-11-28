import sys,fractions,math
fin = open('B-small-attempt1.in','r')
sys.stdout = open('B-small-attempt1.out','w')
T = int(fin.readline())
for cs in range(1,T+1):
    num = [int(x) for x in fin.readline().split(' ')]
    N = num[0]
    del num[0]
    if N==2:
        a = math.fabs(num[0]-num[1])
        if num[0]%a != 0: ans = a-num[0]%a
        else: ans = 0
    else:
        a = math.fabs(num[0]-num[1])
        b = math.fabs(num[1]-num[2])
        c = math.fabs(num[2]-num[0])
        gc = fractions.gcd(a,fractions.gcd(b,c))
        if num[0]%gc != 0: ans = gc-num[0]%gc
        else: ans = 0
    print('Case #%d: %d'%(cs,ans))
fin.close()
