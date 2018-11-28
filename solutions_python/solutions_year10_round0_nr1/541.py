# -*- coding: utf-8 -*-

'''
Created on 2010/05/08

@author: Keniya
'''
from datetime import datetime

def getSmallestN(K):
    if K == 1:
        return 1
    return getSmallestN(K-1)*2 + 1;

def main(filen):

    start = datetime.now()
    
    answers = []
    
    file = open(filen)
    for line in file:
        if (len(line.split()) == 1):
            T = int(line)
            continue
    
        N = int(line.split()[0])
        K = int(line.split()[1])
        if K == 0:
            ans = False
        else:
            ans = (getSmallestN(N) == (K % (getSmallestN(N)+1)) )
        answers.append(ans)
        
    file = open( filen.replace("attempt","answer").replace(".in",".txt"), "w")
    i = 0;
    for ans in answers:
        i += 1
        if ans:
            file.write("Case #" + str(i) + ":" + " ON\n")
        else:
            file.write("Case #" + str(i) + ":" + " OFF\n")
    file.close()
    
    
    end = datetime.now()
    print (end - start)


#filen = "C:\\temp\\A-small-attempt0.in";
#main(filen)

filen = "C:\\temp\\A-large.in";
main(filen)

#filen = "C:\\temp\\A-large-attempt0.in";
#exec(filen)
#
#filen = "C:\\temp\\A-large-attempt0.in";
#exec(filen)