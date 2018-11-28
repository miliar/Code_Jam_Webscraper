'''
Created on May 20, 2011

@author: diego


'''

def gcd(a, b):
    while b != 0:
        (a, b) = (b, a%b)
    return a

def parseCase(n,pd,pg):
    if pg==0 and pd>0:
        return "Broken"
    elif pg==100 and pd<100:
        return "Broken"
    
    if (100/gcd(pd,100)>n):
        return "Broken"
    
    
    return "Possible"

    
        
            
        
        

if __name__ == '__main__':
    file=open('test.dat')
    lines=file.readlines()
    testCases=int(lines[0])
    lines=lines[1:]
    i=1
    while(len(lines)>0):
        line=lines[0]
        line = line.split()
        resp=parseCase(int(line[0]),int(line[1]),int(line[2]))
        print 'Case #' + str(i) + ': ' + str(resp)
        i=i+1
        lines=lines[1:]