#input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

import math

inputs = []
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  inputs.append([n,m])
  #print("Case #{}: {} {}".format(i, n + m, n * m))
  # check out .format's specification for more formatting options



def sol(n, k ):
    a = 1
    i = 0
    while (int(math.pow(2,i))<= k):
        a = int(math.pow(2,i))
        i+=1
    #print(a)
    rem = (k-a+1)
    #print('remainder is '+ str(rem))
    slots = n-a+1
    if slots == 0:
        return [0,0]
    #print('num slots is '+ str(slots))
    spaces = slots//a
    extra = slots % a
    #print(spaces)
    #print(extra)
    if rem <= extra:
        spaces +=1
    result = spaces//2
    if spaces %2 ==0:
        return  [result,result-1]
    else:
        return [result,result]
    

    
for i in range(t):
    solution = sol(inputs[i][0],inputs[i][1])
    print("Case #{}: {} {}".format(i+1,solution[0],solution[1] ))