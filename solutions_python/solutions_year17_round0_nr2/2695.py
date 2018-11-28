# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 15:25:21 2017

@author: noppa
"""


def isTidy(n):  
    # n is string
    length = len(n)
    if length <= 1 :
        return True
    for i in range(length-1):
        if int(n[i]) > int(n[i+1]) :
            return False
    return True

def makeItTidy(n):
    # n is string
    if isTidy(n) :
        return n
    #length = len(n)
    nstr = "".join(n)
    newn = n
    while not isTidy(newn):
        lnewn = len(newn)
        for i in range(lnewn - 1):
            if int(newn[i]) > int(newn[i+1]):
                #newn[i+1] = '9'
                newn = newn[:i+1]+'9'+newn[i+1 +1:]
                if int("".join(newn)) > int(nstr) :
                    newn = newn[:i] + str(int(newn[i]) - 1) + newn[i+1:]                    
    return newn
    

def main():
    path = "C:\\Users\\noppa\\Dropbox\\codejam\\"
    filename = "B-small-attempt0"
    inputfile = open(path+filename+".in", 'r')
    outputfile = open(path+filename+"_ans.in",'w')
    
    noofcase = int(inputfile.readline())
    
    for i in range(1,noofcase+1):
        number = inputfile.readline().replace('\n','')
        print (number)
        number_tidy = makeItTidy(number)
        answernumber = str(int("".join(number_tidy)))        
        answerstring = "Case #"+str(i)+": "+ answernumber
        outputfile.write(answerstring + '\n')
        print(answernumber)
        print("-----------------")
        
    inputfile.close()
    outputfile.close()

main()