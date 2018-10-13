import math
import numpy as np
#dederlein

def P(n,k):
    if (n % 2 == 0) and (k == 1):
        return int(n/2), int(n/2-1)
    elif (n % 2 == 1) and (k == 1):
        return int((n-1)/2), int((n-1)/2)
    elif (n % 2 == 1) and (k % 2 == 1) and (k > 1):
        return P((n-1)/2,(k-1)/2)
    elif (n % 2 == 1) and (k % 2 == 0) and (k > 1):
        return P((n-1)/2,k/2)
    elif (n % 2 == 0) and (k % 2 == 1) and (k > 1):
        return P(n/2-1,(k-1)/2)
    elif (n % 2 == 0) and (k % 2 == 0) and (k > 1):
        return P(n/2,k/2)


def solve(n):

    N = int(n[0])
    k = int(n[1])

    sol = P(N,k)

    s = str(sol[0]) + ' ' + str(sol[1])

    return 1,s






IN = open('Input.txt', 'r')
OUT = open('Output.txt', 'w')

T = int(IN.readline())

for line in range(T):
    # Instanz mit mehreren Zeilen
    yes = 0
    if yes == 0:
        #sizen = int(IN.readline())
        n = list(map(str, IN.readline().split()))
    else:
        T0 = list(map(int, IN.readline().split()))
        #n = list(map(int, IN.readline().split()))
        n = []
        for i in range(T0[0]):
            n.append(list(IN.readline().split()))

    print(solve(n)[1])
    if solve(n)[0] == 1:
        answer = solve(n)[1]# ' '.join(map(str,solve(n)[1]))
        OUT.write('Case #{}: {}\n'.format(line + 1, answer))
    else:
        OUT.write('Case #{}:\n'.format(line + 1))
        for i in range(len(solve(n)[1])):
            answer = solve(n)#' '.join(map(str,solve(n)[1][i]))
            OUT.write('{}\n'.format(answer))
    if yes == 1:
        line -= T0[0]
IN.close()
OUT.close()