#!/usr/bin/python

final_str = "welcome to code jam"

def countOccurances(in_str, char):
    count = 0
    for x in in_str:
        if x == char:
            count += 1
    return count

def findAll(in_str,chr):
    for x in range(0,len(in_str)):
        if in_str[x] == chr:
            yield x

def countSubSeq(input_str, final_str):
    # print input_str, final_str
    if len(final_str) == 0:
        return 0
        
    if len(final_str) == 1:
        return countOccurances(input_str, final_str[0])
        
    firstLetter = final_str[0]
    count = 0
    if (input_str.find(firstLetter) == -1):
        return 0
        
    for i in findAll(input_str, firstLetter):
        count += countSubSeq(input_str[i+1:],final_str[1:])
    return count

N = int(raw_input())

for x in range(0, N):
    input_str = raw_input().strip()
    print "Case #"+str(x+1)+":","%04d" % (countSubSeq(input_str, final_str)%10000)
