import numpy
import sys
import os
def getResult(m, row_size, col_size):
    row_max = [0]*row_size
    col_max = [0]*col_size
    
    if row_size==1 or col_size==1:
        return 1
    
    for i in range(row_size):
        row_max[i] = m[i,:].max()
    for i in range(col_size):
        col_max[i] = m[:,i].max()
    
    r = 1
    for i in range(row_size):
        for j in range(col_size):
            if m[i][j]<row_max[i] and m[i][j]<col_max[j]:
                r=0
    return r

if __name__=='__main__':
    filename = 'B-large.in'
    f = open(filename)
    case_size = -1
    result=[] #0-NO 1-YES
    
    case_count = 0
    row_size = -1
    col_size = -1
    row_count = 0
    
    for line in f:
        line = line.strip()
        if case_size < 0:
            case_size = int(line)
            continue
       
        ll = line.split()      
        
        if col_size<0 and row_size<0:
            row_size = int(ll[0])
            col_size = int(ll[1])
            row_count = 0
            m = numpy.empty((row_size,col_size,))
            continue
        
        if len(ll)!=col_size:
            print 'wrong!'
            sys.exit()
        
        for i in range(0,col_size):
            m[row_count][i] = ll[i]
        row_count+=1
        
        if row_count==row_size:
            result.append(getResult(m, row_size, col_size))
            case_count += 1
            row_size = -1
            col_size = -1  
            
        if case_count == case_size:
            break
    f.close()
    
    resultFile = open('result3_large.txt','w')
    for i in range(len(result)):
        r = result[i]
        s = 'Case #'+str(i+1)+': '
        if r==1:
            s+='YES'
        else:
            s+='NO'
        s+=os.linesep
        resultFile.write(s)
    resultFile.close()
            
        