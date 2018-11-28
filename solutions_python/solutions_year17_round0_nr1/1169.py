import math
import numpy as np
#dederlein
def solve(n):
    s = n[0]
    K = int(n[1])

    sol = 0
    i = 0

    while i<=len(s)-K:
        if s[i] == '+':
            i += 1
        else:
            sol += 1
            for j in range(K):
                if s[i+j] == '-':
                    s = s[:i+j] + '+' + s[i+j+1:]
                else:
                    s = s[:i+j] + '-' + s[i+j+1:]
                print(s)


    if s[-K:] != '+'*K:
        sol = 'IMPOSSIBLE'


    return 1,sol






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

    #print(solve(n)[1])
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