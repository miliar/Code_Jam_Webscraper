#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def multiply(quaternion):
    answer = '1'
    totalSign = 1
    
    
    
    foundi = False
    foundj = False
    foundk = False
    count = 0
    for x in quaternion:
        #print count
        #print "sign = " + str(totalSign)
        #print "answer = " + answer
        sign, answer = calculate(answer, x)
        totalSign *= sign
        
        if (not foundi) and answer == "i" and totalSign == 1:
            foundi = True
            answer = "1"
            totalSign = 1
            #print "foundI"
        elif (not foundj) and foundi and answer == "j" and totalSign == 1:
            foundj = True
            answer = "1"
            totalSign = 1
            #print "foundJ"
        elif (not foundk) and foundj and answer == "k" and totalSign == 1 and count + 1 == len(quaternion):
            foundk = True
            answer = "1"
            totalSign = 1
            #print "foundK"
        count += 1
    if foundi and foundj and foundk:
        return True
    return False
    
    
def calculate(answer, x):
    if answer == '1':
        if x == '1':
            return 1, '1'
        if x == 'i':
            return 1, 'i'
        if x == 'j':
            return 1, 'j'
        if x == 'k':
            return 1, 'k'
    if answer == 'i':
        if x == '1':
            return 1, 'i'
        if x == 'i':
            return -1, '1'
        if x == 'j':
            return 1, 'k'
        if x == 'k':
            return -1, 'j'
    if answer == 'j':
        if x == '1':
            return 1, 'j'
        if x == 'i':
            return -1, 'k'
        if x == 'j':
            return -1, '1'
        if x == 'k':
            return 1, 'i'
    if answer == 'k':
        if x == '1':
            return 1, 'k'
        if x == 'i':
            return 1, 'j'
        if x == 'j':
            return -1, 'i'
        if x == 'k':
            return -1, '1'
'''
print multiply("ik")
print multiply("ijk")
print multiply("kji")
print multiply("jijijijijiji")
print multiply("iiiiiiiiii")
'''
def concatn(ijkstring, times):
    answer = ""
    for x in range(0, times):
        answer += ijkstring
    return answer

f = open("C-small-attempt1.in", "r")
#f = open("C-small-attempt0.in", "r")
#f = open("D.in", "r")

T = int(f.readline())

for x in range(0, T):
    readline = f.readline().split(" ")
    D = int(readline[0])
    L = int(readline[1].strip())
    ijkstring = f.readline().strip()
    #print ijkstring
    answer =  multiply(concatn(ijkstring,L))
    if answer :
        answer = "YES"
    else:
        answer = "NO"
    print "Case #" + str(x+1) + ": " + str(answer)

'''
varchar = ['1', 'i', 'j', 'k']
for x in varchar:
    for y in varchar:
        result = calculate(x, y)
        if result[0] == 1:
            sign = "+"
        else :
            sign = "-"
        print x +" . " + y + " = " +  sign + result[1]
'''