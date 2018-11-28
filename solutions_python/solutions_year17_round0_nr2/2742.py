# -*- coding: utf-8 -*-
#

def istidy(num):
    curm = -1
    for ch in str(num):
        if int(ch) < curm:
            return False
        curm = int(ch)
    return True

t = int(input())
dbg = False   
#dbg = True
fout = open("b2.out", "w")
for i in range(1, t + 1):
    n = int(raw_input().strip()) 
    norig = n
    if n < 10: 
        tmpres = n
    else:
        tmpres = '' 
        while not istidy(n):
            if str(n)[-1:] =='9':
                if dbg: print("endswith 9")
                tmpres =  tmpres + '9'
                n = int(n/10)
                if dbg: print("newn=",n)
            n = n - 1        

        tmpres = str(n) + tmpres
        #print("tmpres=", tmpres)
        
    fout.write("Case #{}: {}\n".format(i,tmpres))
    