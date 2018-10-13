  # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import os
os.chdir("D:/JC/Codejame2017/B")
#import fileinput
#import sys

f = open('B-large.in')
t = int(f.readline())

target = open('q2-L.txt', 'w')


def trials (num):
     klist = [int(j) for j in str(num)]
     length = len(klist)
     flag = 0
     if len(klist) == 1:
         return(num)
     elif all(klist[v] <= klist[v+1] for v in range(length-1)):
         return(num)
     else:
         for p in range(length-1):
             if klist[length-1-p] == klist[length-2-p]:
                 flag = 1
                 continue
             elif klist[length-1-p] < klist[length-2-p]:
                 if flag == 1:
                     klist[length-1-p:] =  [0] * (p+1)
                     res = int(''.join(map(str,klist)))
                     res-=1
                     #print(klist)
                     return trials(res)
                 else:
                     klist[length-1-p] = 9
                     klist[length-2-p] = klist[length-2-p] - 1    
                     klist[length-1-p:] =  [9] * (p+1)
         return trials(int(''.join(map(str,klist))))

for i in range(t):
     k = int(f.readline().strip())
     res = trials(k)
     #print(int(''.join(map(str,klist))))   
     line = "Case #{}: {}".format(i+1, res)     
     if(i <= t-2):         
         target.write(line)
         target.write("\n")
target.write(line)  
target.close()
#   #print("Case #{}: {}".format(i+1, res))    
               
