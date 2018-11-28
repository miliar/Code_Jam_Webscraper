
import math

def encadre(k):
    I = math.floor(math.log(k)/math.log(2))
    return int(I)+1


T = int(input())
for t in range(T):
    N,K = [int(i) for i in input().split()]
    I = encadre(K)
    Z = (N-2**I+1.)/2**I
    fpart = Z-math.floor(Z)
    V = fpart*2**I
    U=2**I-V

    if V < 2**(I-1):
        if K<2**(I-1)+V:
           print("Case #%i:"%(t+1), math.ceil(Z), math.floor(Z))
        else:
           print("Case #%i:"%(t+1), math.floor(Z), math.floor(Z))
    elif V == 2**(I-1):
        print("Case #%i:"%(t+1), math.ceil(Z), math.floor(Z))
    else:
        if K < V: # :)
           print("Case #%i:"%(t+1), math.ceil(Z), math.ceil(Z))
        else:
           print("Case #%i:"%(t+1), math.ceil(Z), math.floor(Z))

