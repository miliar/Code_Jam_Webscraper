import string
import math

input = 'C-small-attempt0.in'
output = 'output-c-small0'
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
    tmp = map(int, string.split(f.readline()))
    a = map(int, string.split(f.readline()))
    
    N = tmp[0]
    L = tmp[1]
    H = tmp[2]
    flag = 0
    
    for j in range(L, H + 1):
        for i in range(N):
            if a[i] % j == 0 or j % a[i] == 0:
                flag = 1
            else:
                flag = 0
                break
        if flag == 1:
            break
                
    if flag == 1:
        out.write('Case #' + str(index + 1) + ': ' + str(j) + '\n')
    else:
        out.write('Case #' + str(index + 1) + ': NO\n')