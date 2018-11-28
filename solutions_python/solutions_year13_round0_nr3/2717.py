# -*- coding: utf-8 -*-
import math

def is_palindrom(number):
    string = str(number)
    n = len(string)
    for k in range(int(round((n-1)/2.0))):
        if string[k]!=string[-1-k] :
            return False
    return True        


f1 = open('fs.in')
f2 = open('fs.out', mode = "w")
i = 0
ss = []
for line in f1 :
    i += 1
    line = line[:-1]
    if i==1 :
        T = int(line)
    else :
        st = line.split()
        A = int(st[0])
        B = int(st[1])
        j = 0
        for x in range(int(math.ceil(math.sqrt(A))),int(math.floor(math.sqrt(B)))+1) :
            if is_palindrom(x) and is_palindrom(x**2):
                j += 1
        ss.append(j)        

for i in range(T):  
    st2 = 'Case #' + str(i+1) + ': ' + str(ss[i]) + "\n"    
    f2.write(st2)

f2.close()
f1.close()            