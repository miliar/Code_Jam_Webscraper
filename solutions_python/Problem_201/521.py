# import numpy as np

def myFunc (big, numBig, numSmall):
    small = big-1
    
    newBig = big/2
    newNumBig = 0
    newNumSmall = 0
    
    if (big%2):
        #big is odd
        newNumBig += 2*numBig
    else:
        newNumBig += numBig
        newNumSmall += numBig
        
    if (small%2):
        #small is odd
        newNumSmall += 2*numSmall
    else:
        newNumBig += numSmall
        newNumSmall += numSmall        
        
    return newBig, newNumBig, newNumSmall

if __name__ == '__main__':
    
    fin = open('C-large.in','r')
    fout = open('output.txt','w')
    
    T = int(fin.readline())
    for t in range(T):
        temp = fin.readline().strip().split(' ')
        stalls = int(temp[0])
        queue = int(temp[1])
                
        i = 0
        
        big = stalls
        numBig = 1
        numSmall = 0
        
        while( (2**i < queue) and (big > 0) ):
            big, numBig, numSmall = myFunc(big, numBig, numSmall)
            #print numBig, " groups of ", big, ", ", numSmall, " groups of ", big-1
            queue -= 2**i
            i+=1
        
        #print "\n", queue
        big -= 1
        if (queue>numBig):
            big -= 1
        
        fout.write('Case #' + str(t+1) + ': ' + str(big/2 + big%2) + ' ' + str(big/2) + '\n')
        #print big/2 + big%2, big/2
         
    
    
    fin.close() 
    fout.close()
    
    print 'done'
    
