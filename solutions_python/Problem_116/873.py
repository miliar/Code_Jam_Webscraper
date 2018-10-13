import numpy
import os

def subtrace(m,T):
    c = 0
    for i in range(0,T):
        c+=m[i][T-i-1]
    return c

def getResult(m, T, dotCount): 
    print 'round:'
    for i in range(0,T):
        rowsum = m[i,:].sum()
        if rowsum == -2.5 or rowsum == -4:
            return 0
        if rowsum == 3.5 or rowsum == 4:
            return 1
        
    for j in range(0,T):
        colsum = m[:,j].sum()
        if colsum == -2.5 or colsum == -4:
            return 0
        if colsum == 3.5 or colsum == 4:
            return 1
    
    d = numpy.trace(m)
    if d == -2.5 or d == -4:
        return 0
    if d == 3.5 or d == 4:
        return 1
    
    d = subtrace(m,T)
    if d == -2.5 or d == -4:
        return 0
    if d == 3.5 or d == 4:
        return 1    
    
    if dotCount:
        return 2
    else:
        return 3
    
if __name__ == '__main__':
    filename = 'A-large.in'
    f = open(filename)
    case_size = -1
    result = [] #0-X won,1-O won,2-not finish,3-draw
    T = 4
    m = numpy.empty((T,T,))
    count = 0
    t = 0
    dotCount = False
    for line in f:
        line = line.strip()
        if case_size < 0:
            case_size = int(line)
            continue
        if line=='':
            continue;
        x = 0
        for ls in line:
            n = 0
            if ls=='X':
                n=-1
            if ls=='O':
                n=1
            if ls=='T':
                n=0.5
            if ls=='.':
                dotCount = True
                n=0
            m[count][x] = n
            x += 1
        count+=1
        
        
        if count==T:
            result.append(getResult(m, T, dotCount))
            dotCount = False
            t += 1
            count = 0
            continue             
        if t==case_size:
            break  
        
    f.close()
    resultFile = open('result1_large.txt','w')
    for i in range(case_size):
        s = 'Case #'+str(i+1)+': '
        r = result[i]
        if r==0:
            s+='X won'
        if r==1:
            s+='O won'
        if r==2:
            s+='Game has not completed'
        if r==3:
            s+='Draw'
        s+=os.linesep
        resultFile.write(s)
    resultFile.close()
        