'''
Created on 2010/05/08
@author: aflc
'''

import sys

def toggle(snps):
    state = True
    for i in range(len(snps)):
        if state:
            state = snps[i]
            snps[i] = not snps[i]
        else:
            break

# all Snapper is ON -> the light will be on.
# True = ON, False = OFF
with open(sys.argv[1], 'r') as fi:
    with open('out.txt', 'w') as fo:
        num = 0
        for s in fi:
            nandk = s.split(' ')
            if len(nandk) == 2:
                num += 1
                n, k = map(int, nandk)
                snappers = [False] * n
                for i in range(k):
                    toggle(snappers)

                res = 'OFF'
                if all(snappers):
                    res = 'ON'
                fo.write('Case #' + str(num) + ': ' + res + '\n')
