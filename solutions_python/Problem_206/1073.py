"""
@author: Kunal Baweja

Google Codejam 2017 Round 1C
"""
from __future__ import print_function

OUTPUT = "Case #%d: %f"

T = int(raw_input().strip())



for j in range(1, T+1):
    D, N = raw_input().strip().split()
    D = float(D)
    N = long(N)

    Km = Sm = tm = 0.0
    for i in xrange(1, N+1):
        K, S = raw_input().strip().split()
        K = float(K)
        S = float(S)

        t = (D - K)/S
        if t > tm:
            tm = t
            Km = K
            Sm = S

    speed = (D * Sm)/(D - Km)
    print(OUTPUT % (j, speed))


