import fractions
import sys
import string
from Numeric import *

line = sys.stdin.readline()
L = line.split()
T = int(L[0])

for t in range(T):
    line = sys.stdin.readline()
    L = line.split()
    N = int(L[0])

    numbers = []
    diffs = []
    
    for i in range(N):
        numbers.append(int(L[1+i]))

    num_gcd = numbers[0]
    for i in range(N):
        num_gcd = fractions.gcd(num_gcd,numbers[i])

    numbers = sort(numbers)

    for i in range(N-1):
        diffs.append(numbers[i+1] - numbers[i])
   
    diff_gcd = diffs[0]
    for i in range(N-1):
        diff_gcd = fractions.gcd(diff_gcd,diffs[i])

    if diff_gcd == num_gcd:
        print "Case #"+str(t+1)+": "+str(0)
    else:
        off =  numbers[0] % diff_gcd
        ans = diff_gcd - off
        print "Case #"+str(t+1)+": "+str(ans)
        

    
    

