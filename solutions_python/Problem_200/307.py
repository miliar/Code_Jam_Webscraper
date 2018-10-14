from __future__ import print_function
# s = """5
# 1325
# 1000
# 1234567
# 111111111111111110
# 111222222222220"""
s = open('B-large.in').read()
import sys
ss = s.split('\n')
N = int(ss[0])
f = open('B.out', 'w')#sys.stdout
for i in range(0, N):
    cs = ss[1+i]
    N = [int(c) for c in cs]
    # print(N)
    first_flip = -1
    first_idx = 0
    first_n = N[0]
    for n in range(0, len(N)-1):
        if N[n] == first_n:
            pass
        elif N[n] > first_n:
            first_idx = n
            first_n = N[n]
        if N[n] > N[n+1]:
            first_flip = n
            break
    if first_flip == -1:
        out = N
    else:
        # print(first_flip)
        out = N
        out[first_idx] -= 1
        for j in range(first_idx+1, len(N)):
            out[j] = 9
    lead_zero_idx = 0
    for j in out:
        if j == 0:
            lead_zero_idx += 1
        else:
            break
    out = out[lead_zero_idx:]
    print( ('Case #%d: '%(i+1) + ''.join([str(c) for c in out])+"\n"), end="", file=f)