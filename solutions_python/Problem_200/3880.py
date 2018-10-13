# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems. 
from collections import deque
def checknondecreasing(s):
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True
def fill(s,c):
    for i in range(c+1, len(s)):
        s[i] = 9
def decrement(s,c):
    if c == 0:
        if s[c] != 1:
            s[c] -= 1
            fill(s,c)
        else:
            fill(s,c-1)
            del s[-1]
    
    else:
        if s[c] > 0:
            s[c] -= 1
            fill(s,c)
        else:
            s[c] = 9
            fill(s,c)
            decrement(s,c-1)
def calc(n): 
    s = [int(d) for d in str(n)]
    r = s[:]
    c = 0
    while not checknondecreasing(s):
        if s[c] <= s[c+1]:
            c += 1
        else:
            decrement(s, c)  
            c = 0
     
        
    
    
    return int(''.join(map(str,s)))
with open('input', 'r') as f:
    t = int(f.readline())
    for i in range(1, t + 1):
      n = f.readline()  # read a list of integers, 2 in this case
      r = calc(int(n))
      print("Case #{}: {}".format(i, r))
  # check out .format's specification for more formatting options
  
  
"""
4
132
1000
7
111111111111111110
"""