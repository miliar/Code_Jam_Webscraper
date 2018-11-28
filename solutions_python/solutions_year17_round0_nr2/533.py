# import numpy as np

if __name__ == '__main__':
    
    fin = open('B-large.in','r')
    fout = open('output.txt','w')
    
    T = int(fin.readline())
    for t in range(T):
        numString = fin.readline().strip()
        l = len(numString)
        
        output = ''
        for i in range(l-1,0,-1):
            if (numString[i-1] > numString[i]):
                numString = numString[:i-1]+str(int(numString[i-1])-1)+'9'*len(numString[i:])

        fout.write('Case #' + str(t+1) + ': ' + str(int(numString)) + '\n')
    
    fin.close() 
    fout.close()
    print 'done'
    
