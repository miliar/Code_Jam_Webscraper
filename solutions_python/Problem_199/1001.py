# python2
import sys
import math

    
class main():
    T = int(sys.stdin.readline().rstrip())
    
    for t in range(T):
        line = sys.stdin.readline().rstrip()
        temp = line.split()
        K = int(temp[1])
        S = temp[0].rstrip()
        N = len(S)
        
        A = []
        for i in range(N):
            if (S[i] == '+'):
                A.append(1)
            else:
                A.append(0)
                
        N_flip = 0
        while True:
            for i in range(N):
                if (A[i] == 0):
                    break
            if (A[i] == 1):
                print "Case #" + str(t+1) + ": " + str(N_flip)
                break
            else:
                N_flip = N_flip + 1
                if (i + K > N):
                    print "Case #" + str(t+1) + ": " + "IMPOSSIBLE"
                    break
                for j in range(K):
                    A[i+j] = 1 - A[i+j]
