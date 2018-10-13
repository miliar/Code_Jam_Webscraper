'''
Created on 03/05/2014

@author: user3
'''


def processCase(t, A, B, K):
    
    n = 0;
    for i in range(A):
        for j in range(B):
            if (i&j) < K:
                n = n + 1
            
    
    print('Case #' + str(t+1) + ": " + str(n))
    return 'Case #' + str(t+1) + ": " + str(n) + '\n'


if __name__ == '__main__':
    myinput = open('1AB-small-attempt0.in', 'r')
    myoutput = open('1AB-small-attempt0.out', 'w')
    
    
    T = int(myinput.readline())
    
    for t in range(T):
        A, B, K = map(int, myinput.readline().split())
        myoutput.write(processCase(t, A, B, K))
    
    myoutput.close()
    myinput.close()
    pass