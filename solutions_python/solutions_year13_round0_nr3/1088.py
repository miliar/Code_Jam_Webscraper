'''
Created on 2013/4/13

@author: arbiter
'''
import math
def A():
    fileopen = open('C-small-attempt0.in')
    line = fileopen.readline()
    T=int(line)
    an=0
    
    while T>0:
        T=T-1
        an=an+1
        line = fileopen.readline()
        n = int(line.split('\n')[0].split(' ')[0])
        m = int(line.split('\n')[0].split(' ')[1])
        ans=0
        for i in range(n,m+1):
            if math.sqrt(i)==int(math.sqrt(i)):
                tmp = str(i)
                ok=1
                for j in range(len(tmp)):
                    if tmp[j]!=tmp[-j-1]:
                        ok=0
                        break
                tmp = str(int(math.sqrt(i)))
                for j in range(len(tmp)):
                    if tmp[j]!=tmp[-j-1]:
                        ok=0
                        break 
                    
                if ok==1:
                    ans=ans+1
        print 'Case #%d: %d' % (an,ans)

    fileopen.close()

if __name__=='__main__':
    A()
