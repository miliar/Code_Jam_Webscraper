# import numpy as np

if __name__ == '__main__':
    
    fin = open('A-large.in','r')
    fout = open('output.txt','w')
    
    T = int(fin.readline())
    for t in range(T):
        temp = fin.readline().strip().split(' ')
        cakes = temp[0].strip()
        l = len(cakes)
        flipper = int(temp[1])
        
        isFlipped = [False]*flipper
                
        flipCount = 0
        
        for i in range(l+1-flipper):
            if ( (cakes[i]=='-' and not isFlipped[0]) or (cakes[i]=='+' and isFlipped[0]) ):
                #must flip
                flipCount += 1
                #flip all
                isFlipped = [not f for f in isFlipped]
            #move on to next cake
            isFlipped.pop(0)
            isFlipped.append(False)
        
        output = str(flipCount)
        
        #check last cakes that cannot be fixed
        for i in range(l+1-flipper, l):
            if ( (cakes[i]=='-' and not isFlipped[0]) or (cakes[i]=='+' and isFlipped[0]) ):
                output = "IMPOSSIBLE"
            isFlipped.pop(0)
            
        fout.write('Case #' + str(t+1) + ': ' + output + '\n')
    
    fin.close() 
    fout.close()
    print 'done'
    
