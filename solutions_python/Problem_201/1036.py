
  # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import os
import math
os.chdir("D:/JC/Codejame2017/C")
#import fileinput
#import sys

f = open('C-small-2-attempt0.in')
t = int(f.readline())

target = open('q3s2.txt', 'w')
             
for i in range(t):
    n,k = f.readline().strip().split(" ")
    n,k = [int(n),int(k)]
    if (k == 1 and n % 2 == 1):
        ans = (n+1)/2-1
        ans1 = (n+1)/2-1
    elif (k == 1 and n % 2 == 0):
        ans = (n/2)
        ans1 = (n/2)-1
    else:
        b = list(bin(k))
        rev = b[::-1]
        for q in range(len(rev)-3):
            if rev[q] == '1':
                n = math.floor((n-1)/2)
            else:
                n = math.ceil((n-1)/2)
        if(n%2 == 1):
            ans = (n-1)/2
            ans1= ans
        else:
            ans = n/2
            ans1 = ans-1
    line = "Case #{}: {} {}".format(i+1, int(ans), int(ans1))
    if (i <= t-2):
         target.write(line)
         target.write("\n")
target.write(line)  
target.close()    
    
    