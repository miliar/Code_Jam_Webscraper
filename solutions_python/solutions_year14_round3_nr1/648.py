# New Lottery Game 

import math
import time

def gcd(a,b):
    while a:
        a, b = b%a, a
    return b

time_start = time.time()

file_input = open('A-small-attempt0.in')
file_out = open('Out1.txt','w')
file_out.write('')
file_out.close()

Test_Cases = [int(a) for a in file_input.readline().split(' ')][0]
print(Test_Cases)
N = 1

Q_min = 1/(2E40)

n = 0

while N <= Test_Cases:

    row1 = [int(a) for a in file_input.readline().split('/')]

    P = row1[0]
    Q = row1[1]

    GCD = gcd(P,Q)

    P = int(P/GCD)
    Q = int(Q/GCD)

    log2 = math.log(Q,2)

    if log2 == math.floor(log2) and Q >= Q_min:

        Gens_back = 1

        P_new = P
        Q_new = Q

        while P_new/Q_new < 0.5:

            Gens_back += 1

            P_new = P_new*2
        
        file_out = open('Out1.txt','a')
        file_out.write('Case #'+str(N)+': '+str(Gens_back)+'\n')
        file_out.close()

    else:

        file_out = open('Out1.txt','a')
        file_out.write('Case #'+str(N)+': impossible\n')
        file_out.close()

    #print('Case #'+str(N)+': '+str((K-1)*(K-1)+win_counts))

    N+=1

time_end = time.time()

print('Time taken is: '+str(time_end-time_start)+' sec')

print(gcd(123,31488))
