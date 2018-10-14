'''
Created on Apr 14, 2013

@author: camgelo
'''
import sys

def isFair(s):
    if s==s[::-1]:
        return True
    return False

def genFairAndSquare(n):
    lst=[1,4,9]
    i=10
    while i<=n:
        s=str(i)
        if len(s)>3 and int(s[0])>3:
            i=10**len(s)
        if isFair(s) and isFair(str(i*i)):
            lst.append(i*i)
            #print i,i*i
            if (i*i)>n:
                break
        i+=1
    print lst
    print 'size:',len(lst)
    return lst

def handle(lst, start, end):
    result=[]
    print start,"~",end
    for n in lst:
        if n>=start and n<=end:
            result.append(n)
    print result
    return str(len(result))

def main(lst):
    f=file(sys.argv[1])
    num = int(f.readline().strip())
    output=file('output.txt','wb')
    for count in range(1, num+1):
        start,end=map(int,f.readline().strip().split(' '))
        result = handle(lst, start,end)
        print "Case #%s: %s"%(count,result)
        print 
        output.write("Case #%s: %s\r\n"%(count,result))

if __name__=='__main__':
    import time
    s=time.time()
    lst = genFairAndSquare(10**15)
    main(lst)
    print 'spent',time.time()-s