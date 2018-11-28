
def get_res(D, N, L):
       Ls = sorted(L, key=lambda x: D-x[0])
       x0, v0 = Ls[0]
       Tmax = float(D-x0)/v0
       for i in range(1, N):
           xa, va = L[i-1]
           xb, vb = L[i]
           Ta = float(D-xa)/va
           Tb = float(D-xb)/vb
           if Tb > Ta:
               Tmax = Tb 
       return float(D)/Tmax

def get_res_lin(D, N, L):
       x0, v0 = L[0]
       Tmax = float(D-x0)/v0
       for i in range(1, N):
           xa, va = L[i]
           Ta = float(D-xa)/va
           if Ta > Tmax:
               Tmax = Ta 
       return float(D)/Tmax


t = int(raw_input())  
for i in xrange(1, t + 1):
    D, N = [int(s) for s in raw_input().split(" ")]
    L = []
    for j in range(N):
        Ki, Si = [int(s) for s in raw_input().split(" ")]
        L.append((Ki, Si))
    result = get_res_lin(D, N, L)
    print "Case #{}: {}".format(i, result)
