#Name: Robin Park
#Username: robinp
#Google Code Jam Round 1B 2017

import random
import math

def solve(D, N, KS_tuples):
    answer = 0
    
    max_time = (D-KS_tuples[0][0]) / float(KS_tuples[0][1])

    for k in range(1, len(KS_tuples)):
        if KS_tuples[k][1] <= KS_tuples[k-1][1] or (KS_tuples[k-1][0] - KS_tuples[k-1][0]) / float(KS_tuples[k][1] - KS_tuples[k-1][1]) > max_time:
            max_time = max(max_time, (D-KS_tuples[k][0]) / float(KS_tuples[k][1]))

    answer = D/max_time
    
    w.write('Case #' + str(t+1) + ': ')
    #w.write(''.join(cake[i]))
    w.write(str(answer))
    w.write('\n')


if __name__ == '__main__':
    with open('cruise.in', 'r') as file, open('cruise.out', 'w') as w:  
        T = int(file.readline().strip())
        for t in range(T):
        
            D, N = map(int, file.readline().strip().split())
            KS_tuples = []

            for i in range(N):
                temp1, temp2 = map(int, file.readline().strip().split())
                KS_tuples.append((temp1, temp2))
                
            solve(D, N, KS_tuples)


print("done")
