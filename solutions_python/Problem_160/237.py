# Import the file
with open('B-small-attempt0.in','r') as f:
    data = f.readlines()

# Format the data
T = int(data[0])
del data[0]

from functools import reduce

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)

OUT = []
for i in range(T):
    # Get position in line
    N = [int(el) for el in data[0].split(' ')][1]
    del data[0]
    # Get service rates
    M = [int(el) for el in data[0].split(' ')]
    del data[0]
    # Find cycle length
    CL = lcmm(*M)
    # Find out how many are served in each cycle
    SCL = sum([CL//el for el in M])
    # Find out real N for finding server
    N2 = N%SCL if N%SCL > 0 else SCL
    # Simulate until your turn
    ST = [0]*len(M)
    for jk in range(N2-1):
        I = ST.index(min(ST))
        ST[I] += M[I]
    OUT.append(ST.index(min(ST))+1)
    print(N,N2,M,CL,SCL)

with open('B.out','w') as f:
    for i in range(T):
        f.write('Case #{0}: {1}\n'.format(i+1,OUT[i]))
