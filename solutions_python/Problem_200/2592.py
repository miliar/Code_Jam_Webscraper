# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 10:48:24 2017

@author: Henry
"""

def tidy(N):
    N = str(N)
    N= list(N)
    for i in range(len(N)-1):
        if int(N[i]) > int(N[i+1]):
            return False
    return True
    
def maketidynaive(N):
    while not tidy(N):
        N = N-1
    return N

def maketidy(N):
    N = str(N)
    N = list(N)
    N = [int(i) for i in N]
    cur_digit = 0
    index = 0
    for i, no in enumerate(N):
        if no != cur_digit:
            if no > cur_digit:
                cur_digit = no
                index = i
            else:
                N[index] = cur_digit - 1
                for j in range(index+1, len(N)):
                    N[j] = 9
                
    N = [str(i) for i in N]
    N = ''.join(N)
    return int(N)

N = input()
for i in range(int(N)):
    print('Case #{}: {}'.format(i+1, maketidy(int(input()))))

#tests = [8, 123, 555, 224488, 20, 321, 495, 999990,132,1000,7, 111111111111111110]
#for N in tests:
#    print(maketidy(N), maketidynaive(N))
