import os
import sys
from itertools import *

def powerset(seq): 
    if len(seq) <= 1: 
        yield seq 
        yield [] 
    else: 
        for item in powerset(seq[1:]): 
            yield [seq[0]]+item
            yield item 

def main() :
    f=open("C-large.in")
    all_lines = f.readlines()
    case = 1
    for n in range(2,len(all_lines),2) :
        input = all_lines[n].split(" ")
        best_sum = fast(input)
        if best_sum==None :
            best_sum = "NO"
        print "Case #"+str(case)+": "+str(best_sum)
        case=case+1

def fast(input) :
    numbers = []
    for i in input :
        numbers.append(int(i))
   # print numbers
    numbers.sort()
    leng = len(numbers)
    xor = reduce(lambda x,y: x^y , numbers)
    lxor = 0 
    rxor = xor 
    
    if len(numbers)==2 :
        if numbers[0]==numbers[1] :
            return numbers[0]

    for i in range(1,len(numbers)-1) :
        lxor = reduce(lambda x,y: x^y , numbers[0:i])
       # print numbers[i-1]
        rxor = rxor ^ numbers[i-1]
        if lxor == rxor :
            return sum(numbers[i:])

def FIND_XOR(input) :
    numbers = []
    for i in input :
        numbers.append(int(i))
   # print numbers
    numbers.sort()
    leng = len(numbers)
    ls = range(0,leng)
    all = set(ls)
    l= powerset(ls)
    c=0
    max =0 
    bc = []
    bi = []
    for i in l:
        n_list = []
        p_list = []
        s=set(i)
        neg = all - s 
        neg_indices = list(neg)
        for n in neg_indices :
            n_list.append(numbers[n])
        for p in i :
            p_list.append(numbers[p])
       
        if p_list==[] :
            xor_sum=0
        else :
            xor_sum = reduce(lambda x,y: x^y , p_list)
       
        sump= sum(p_list)
        if n_list==[] :
            other_xor_sum = 0
        else :
            other_xor_sum = reduce(lambda x,y:x^y , n_list)
       
        if xor_sum == other_xor_sum and n_list!=[] and p_list!=[]:
            if sump > max :
                max = sump
                bc = p_list 
                bi = i
                print "xor"+str(xor_sum)
                
    print bc
    print bi
    return max
    print str(max)

if __name__ == "__main__" :
    main()


