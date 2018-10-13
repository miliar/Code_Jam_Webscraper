import sys
import copy

def snap(chain, power, n):
    chain2=copy.copy(chain)
    power2=copy.copy(power)
    for i in range(n):
        if power[i]  and chain[i]:
            chain2[i] = False
            power2[i+1] = False
        elif power[i]  and not chain[i]:
            chain2[i] = True
            power2[i+1] = True
        elif not power[i]:
            
            break
    power[0] = True
    return chain2, power2

T = int(sys.stdin.readline())

for t in range(T):
    
    n, k = [int(num) for num in sys.stdin.readline().split()]

    chain = [False] * n
    power = [True] + [False] * (n)

    for kk in range(k):
        chain, power = snap(chain, power, n)

    
    result = 'OFF' if not all(power) else 'ON' 

    print 'Case #{0}: {1}'.format(t+1, result)
