import string
import math

input = 'C-small-attempt0.in'
output = 'output-c-small'
try:
    f = open(input, 'r')
except:
    exit('file: ' + input + ' non trovato')
try:
    out = open(output, 'w')
except:
    exit('file: ' + output + ' non trovato')

T = int(f.readline())

for index in range(T):
    N = int(f.readline())
    l1 = map(int, string.split(f.readline()))
    l3 = l1[:]
    l3.sort()
    l2 = []
    i = 0
    k = 1
    max1 = -1
    while len(l2) < N: 
        l2.append(l3[0])
        del l3[0]
        while i < len(l2):
            j = 0
            while j < len(l3):
                l2[i], l3[j] = l3[j], l2[i]
                xor1 = 0
                tot1 = 0
                for x in l2:
                    xor1 = xor1 ^ x
                    tot1 = tot1 + x
                xor2 = 0
                tot2 = 0
                for x in l3:
                    xor2 = xor2 ^ x
                    tot2 = tot2 + x
                if xor1 == xor2:
                    max1 = max(tot1, tot2, max1)
                j = j + 1
            i = i + 1
    if (max1 == -1):
        out.write('Case #' + str(index + 1) + ': NO\n')
    else:
        out.write('Case #' + str(index + 1) + ': ' + str(max1) + '\n')