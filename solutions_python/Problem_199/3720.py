import numpy as np
import re




def funk1(lst,i,k):
    for j in range(i,i+ k):
        if i + k > len(lst):
            break
        if lst[j] == '-':
            lst[j] = '+'
        elif lst[j] == '+':
            lst[j] = '-'
    return lst

    
def main(stringa, k):
    
    x = list(stringa)
    if len(x) < k:
        return 'IMPOSSIBLE'
    num = 0
    for i in range(len(x)):
        if x[i] == '-':
            x = funk1(x,i,k)
            num = num + 1
    for i in range(len(x)):
        if x[i] != '+':
            return 'IMPOSSIBLE'

    return num



t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    stringa, k = input().split(" ") 
    k = int(k)
    result = main(stringa,k)
    print("Case #{}: {}".format(i, result))

