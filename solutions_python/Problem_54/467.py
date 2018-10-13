from fractions import *
from sys import *
fout = file('ans','w')

if __name__ == '__main__':
    t = int(stdin.readline())
    c = 1
    while t>0:
        t-=1
        info = stdin.readline()
        info = info.split(' ')
        num = []
        diff = []
        for i in range(1,len(info)):
            num.append(int(info[i]))
        n = len(num)
        for i in range(n):
            for j in range(i+1,n):
                diff.append(num[i]-num[j])
        if len(diff)>=2:
            now = gcd(diff[0],diff[1])
        else:
            now = diff[0]
        for i in range(2,len(diff)):
            now = gcd(now,diff[i])
        now = abs(now)
        ans = num[0]%now
        if ans!=0:
            ans = now-ans
        fout.write('Case #%d: %d\n'%(c,ans))
        c += 1
        
        