'''
Created on Apr 8, 2017

@author: piesa
'''
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, m = [s for s in input().split(" ")]  # read a list of integers, 2 in this case
    m = int(m)
    n = list(n)
    count = 0
    flipcount = 0
    minus = False
    while count <= len(n) - m:
        if n[count] == '+':
            count = count + 1
            continue
        if n[count] == '-':
            minus = True
            for j in range(m):
                if n[count+j] == '-':
                    n[count+j] = '+'
                else:
                    n[count+j] = '-'
            count = count + 1        
            flipcount = flipcount + 1
        if  '-' not in n:
            break
    if '-' not in n:
        print("Case #{}: {}".format(i, flipcount))   
    else:
        print("Case #{}: IMPOSSIBLE".format(i))