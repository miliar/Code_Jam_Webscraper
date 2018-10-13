from __future__ import print_function, division
import sys

cases = int(sys.stdin.readline())

for n in range(1, cases+1):
    C, F, X = [float(num) for num in sys.stdin.readline().strip().split()]
    time = 0
    cookiesPS = 2
    
    while True:
        t = X/cookiesPS
        ty = C/cookiesPS + X/(cookiesPS+F)
        if t<=ty: #no need to buy a farm
            time += t
            print('Case #'+repr(n)+': '+'%.7f'%(time))
            break
        else: #hava to buy a farm
            time += C/cookiesPS
            cookiesPS += F
