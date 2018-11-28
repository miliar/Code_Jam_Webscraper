import fractions
import math

file = open('A-small-attempt0.in', 'r')
output = open('output', 'w')

T = file.readline()


def simplify(P, Q):
    g = fractions.gcd(P, Q)
    q = Q / g
    p = P / g
    if q==2:
        return 1
    elif q/2 < p:
        return min(simplify(p-int(q/2),q),simplify(int(q/2),q))
    else:
        return 1+simplify(p, int(q/2))
    
for x in range(1, int(T)+1):
    [P, Q] = list(map(lambda x: int(x), file.readline().replace('\n', '').split('/')))
    
        
    q = int(Q / fractions.gcd(P, Q))
    p = int(P / fractions.gcd(P, Q))
    h = math.log(q, 2)
    if not h == int(h):
        answer = "impossible"
    else:  
        answer = str(simplify(p,q))
        
    solution = 'Case #' + str(x) + ': ' + answer + '\n'
    if x == int(T):
        solution.replace('\n', '')
    output.write(solution)
    print(solution)