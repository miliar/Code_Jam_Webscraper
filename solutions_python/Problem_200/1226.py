import math
import numpy as np
#dederlein

def solve(n):

    s = n[0][::-1]

    for i in range(len(s)-1):
        if int(s[i]) < int(s[i+1]) and i+2 <= len(s)-1:
            q = int(s[i+1])-1
            s = (i+1)*'9' + str(q) + s[i+2:]
        elif int(s[i]) < int(s[i+1]) and i+2 > len(s)-1:
            q = int(s[i+1])-1
            s = (i+1)*'9' + str(q)

    sol = s[::-1]
    if sol[0] == '0':
        sol = sol[1:]

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