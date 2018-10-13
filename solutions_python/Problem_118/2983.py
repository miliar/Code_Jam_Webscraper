import math
import numpy as np

def fairandsquare(A,B):
    A = np.int64(A)
    B = np.int64(B)
    
    AA = np.int64(math.ceil(math.sqrt(A)))
    BB = np.int64(math.floor(math.sqrt(B)))
    
    x = np.int64()
    c=0
    for x in range(AA,BB+1):
        s = str(x)
        if s==s[::-1]:
            y = np.int64(x*x)
            s = str(y)
            if s==s[::-1]:
                c += 1
    
    return c

def run(input,output):
    
    fin = open(input,'r')
    fout = open(output,'w')
    
    # get number of test cases
    T = int(fin.readline())
    
    print "got " + str(T) + " test cases"
    
    for i in range(T):
        s = fin.readline().split(' ')
        A = np.int64(s[0])
        B = np.int64(s[1])
        print "doing test case " + str(i) + " A=" + str(A) + " B=" + str(B)
        
        c = np.int64(fairandsquare(A,B))
        
        fout.write("Case #" + str((i+1)) + ": " + str(c) + '\n')
    
    fin.close()
    fout.close()
    
    
if __name__ == '__main__':
    pass

run('C-small-attempt0.in','C-small-attempt0.out')
    

    
    
