# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 23:22:39 2017

@author: noppa
"""
def flip(pk):
    n = ''    
    for f in pk :
        if f == '+' :
            n += '-'
        elif f == '-' :
            n += '+'
    return n
            


def main():
    path = "C:\\Users\\noppa\\Dropbox\\codejam\\"
    filename = "A-large"
    fformat = ".in"
    inputfile = open(path+filename+fformat, 'r')
    outputfile = open(path+filename+"_ans" + fformat,'w')
    
    noofcase = int(inputfile.readline())
    
    for i in range(1,noofcase+1):
        line = inputfile.readline().replace('\n','')
        pancake, psize = line.split(" ")
        k = int(psize)
        count  = 0
        start = 0
        pk = pancake[start:]
        while True:            
            start = pk.find('-')                        
            if start == -1 or start > (len(pancake) - k):
                #print(pk)
                break
            flipped = flip(pk[start:start+k])
            newpk = pk[:start] + flipped + pk[start+k:]
            count += 1            
            pk = newpk
            #print(pk)
            #print(pancake)
        
        if pk.find('-') != -1 :
            answer = "IMPOSSIBLE"
        else :
            answer = str(count)
                
        answernumber = answer
        print(answernumber)
        answerstring = "Case #"+str(i)+": "+ answernumber
        outputfile.write(answerstring + '\n')
        
        
        
    inputfile.close()
    outputfile.close()

main()