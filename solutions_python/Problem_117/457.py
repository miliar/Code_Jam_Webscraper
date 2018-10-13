'''
Created on Apr 13, 2013

@author: camgelo
'''
import sys

def handle(n,m,lines):
    target=n*m
    count=0
    dicDone={}
    for i in range(n):
        h = 0
        subCount=0
        dicTmp={}
        for j in range(m):
            x=lines[i][j]
            key='%s.%s'%(i,j)
            if x==h and key not in dicDone:
                dicTmp[key]=x
                subCount+=1
            elif x>h:
                h=x
                if key not in dicDone:
                    subCount=1
                    dicTmp={key:x}
                else:
                    subCount=1
                    dicTmp={key:x}
                    
        print "row %s get %s point"%(i+1,subCount)
        count+=subCount
        dicDone.update(dicTmp)
        if count==target:
            return 'YES'
            
    for j in range(m):
        h = 0
        subCount=0
        dicTmp={}
        for i in range(n):
            x=lines[i][j]
            key='%s.%s'%(i,j)
            if x==h and key not in dicDone:
                dicTmp[key]=x
                subCount+=1
            elif x>h:
                h=x
                if key not in dicDone:
                    subCount=1
                    dicTmp={key:x}
                else:
                    subCount=0
                    dicTmp={}
        print "column %s get %s point"%(j+1,subCount)
        count+=subCount
        dicDone.update(dicTmp)
        if count==target:
            return 'YES'    
    print 'total point: %s/%s'%(count,target)
    return 'NO'

def main():
    f=file(sys.argv[1])
    num = int(f.readline().strip())
    output=file('output.txt','wb')
    for count in range(1, num+1):
        n,m=map(int,f.readline().strip().split(' '))
        lines=[]
        for row in range(n):
            lines.append(map(int,f.readline().strip().split(' ')))
            print lines[row]
        result = handle(n,m,lines)
        print "Case #%s: %s"%(count,result)
        print 
        output.write("Case #%s: %s\r\n"%(count,result))

if __name__=='__main__':
    main() 