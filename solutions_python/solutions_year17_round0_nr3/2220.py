# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:48:48 2017

@author: noppa
"""
import math
import collections as ct

def decompose(n, level):
    if level == 0:
        return [n]
    if n == 1 :
        return [0]
    if n % 2 == 0:
        return decompose(n/2 - 1, level-1) + decompose(n/2, level-1)
    else :
        return decompose((n-1)/2, level-1) + decompose((n-1)/2, level-1)
    



def main():
    path = "C:\\Users\\noppa\\Dropbox\\codejam\\"
    filename = "C-small-2-attempt1"
    fformat = ".in"
    inputfile = open(path+filename+fformat, 'r')
    outputfile = open(path+filename+"_ans" + fformat,'w')
    
    noofcase = int(inputfile.readline())
    
    for i in range(1,noofcase+1):
        line = inputfile.readline().replace('\n','')
        ns,ks = line.split(" ")
        n = int(ns)
        k = int(ks)
        level = int(math.floor(math.log2(k)))
        dist = decompose(n, level)
        posinlevel = k - int(2**level)
        sorteddist = sorted(dist)
        sorteddist.reverse()
        ans = decompose(sorteddist[posinlevel], 1)        
        
        #for j in range(k):
        
        answernumber = str(int(max(ans))) + " " + str(int(min(ans)))
        print(answernumber)
        answerstring = "Case #"+str(i)+": "+ answernumber
        outputfile.write(answerstring + '\n')
        
        
        
    inputfile.close()
    outputfile.close()

main()