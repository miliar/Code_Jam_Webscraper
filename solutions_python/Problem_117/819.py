'''
Created on 2013/4/13

@author: arbiter
'''
def A():
    fileopen = open('B-large.in')
    line = fileopen.readline()
    T=int(line)
    an=0
    while T>0:
        T=T-1
        an=an+1
        line = fileopen.readline()
        n = int(line.split('\n')[0].split(' ')[0])
        m = int(line.split('\n')[0].split(' ')[1])
        a = []
        a2 = []
        for i in range(n):
            line = fileopen.readline()
            a.append(line.split('\n')[0].split(' '))
        
        for i in range(n):
            for j in range(m):
                a[i][j]=int(a[i][j])
        for i in range(m):
            t=[]
            for j in range(n):
                t.append(a[j][i])    
            a2.append(t)
#        print a
#        print a2
        t = []
        for i in range(n):
            tmp = []
            for j in range(m):
                tmp.append(100)
            t.append(tmp)
        
        for i in range(n):
            for j in range(m):
                if t[i][j]>max(a[i]):
                    t[i][j]=max(a[i])
        
        for i in range(m):
            for j in range(n):
                if t[j][i]>max(a2[i]):
                    t[j][i]=max(a2[i])
                    
        ok=1
        for i in range(n):
            for j in range(m):
                if t[i][j] != a[i][j]:
                    ok=0
                    break
            if ok==0:
                break
        print 'Case #%d: ' % an,
#        print t
        if ok==1:
            print 'YES'
        else:
            print 'NO'
    fileopen.close()

if __name__=='__main__':
    A()
