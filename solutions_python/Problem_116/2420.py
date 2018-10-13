'''
Created on Apr 5, 2013

@author: swex
'''


prints=["X won","O won","Draw","Game has not completed"]


def detect_in_zip(line):
    if len(line) < 3:
            if 'T' in line and 'X' in line:
                return prints[0]
            if 'T' in line and 'O' in line:
                return prints[1]
            if len(line)==1:
                if 'O' in line:
                    return prints[1]
                if 'X' in line:
                    return prints[0]
    

def solve(case):
    x= zip(*(zip(*case)))
    y=zip(*x)
    for i in range(4):
        xs=set(x[i])
        ys=set(y[i])
        if detect_in_zip(xs) is not None:
            return detect_in_zip(xs)
        if detect_in_zip(ys) is not None:
            return detect_in_zip(ys)
    diag=[]
    for i in range(4):
        diag.append(case[i][i])
    diag=set(diag)
    if detect_in_zip(diag) is not None:
        return detect_in_zip(diag)
    diag=[]
    for i in range(4):
        diag.append(case[3-i][i])
    diag=set(diag)
    if detect_in_zip(diag) is not None:
        return detect_in_zip(diag)
    dots=[j for i in x for j in i]
    if '.' in dots:
        return prints[3]
    else:
        return prints[2]
    
            
    
f=open("/tmp/case")


num=int(f.readline())
#print 'cases = ' + str(num)   
for i in range(1,num+1):
    case=[]
    for j in range(4):
        case.append(f.readline()[:4])
    print "Case #" + str(int(i))+":",solve(case)
    f.readline() #pass \n line


    