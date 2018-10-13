'''
Created on 12/04/2014

'''



def processCase(t, C, F, X):

    y = 0.0
    n = 0
    while True:
        nextF = C / (2 + n * F)
        nextX = X / (2 + n * F)
        
        nextX2 = nextF + X/(2 + (n+1)*F) # Next X with 'n+1' farms
        
        if nextX <= nextX2:
            y += nextX
            break
        else:
            y += nextF
            n += 1
            
    print('Case #' + str(t+1) + ": " + '%.7f' % y)
    return 'Case #' + str(t+1) + ": " + '%.7f' % y + '\n'
    

if __name__ == '__main__':
    myinput = open('B-large.in', 'r')
    myoutput = open('B-large.out', 'w')
    
    T = int(myinput.readline())
    
    for t in range(T):
        C, F, X = map(float, myinput.readline().split())
        myoutput.write(processCase(t, C, F, X))
    
    myoutput.close()
    myinput.close()
    pass