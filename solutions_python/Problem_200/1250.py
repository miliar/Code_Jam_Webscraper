from math import *
def f(n):
    s = str(n)

    broke = False
    if len(s) == 1:
        return n
    for i in range(1,len(s)):
        if int(s[i]) >= int(s[i-1]):
            continue
        else:
            broke = True
            break

    if not broke:
        return n
    else:
        i -= 1
        while int(s[i-1]) == int(s[i]) and i >= 1:
            i -= 1
        if i == 0:
            if s[i] == '1':
                return '9'*(len(s)-1)
            else:
                return str(int(s[0])-1)+'9'*(len(s)-1)
        return int(s[:i] + str(int(s[i])-1) + '9'*(len(s)-i-1))
    
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = input().strip()  # read a list of integers, 2 in this case
    #print(n)
    print("Case #{}: {}".format(i, f(n)))
  # check out .format's specification for more formatting options
