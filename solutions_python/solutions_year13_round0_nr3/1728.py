'''
Created on 2013-4-13

@author: t
'''

import math


def isPalindrome(a):
    a = str(a)
    if a == a[::-1]:
        return True
    else:
        return False
    
    
def test(a,b):
    begin = math.sqrt(a)
    begin_int = int(begin)
    if begin_int == begin:
        begin = int(begin_int)
    else:
        begin = int(begin_int)+1
    
    end = int(math.sqrt(b))
    
    
    num = 0
    
    for i in range(begin,end+1):
        if isPalindrome(i):
            if isPalindrome(i**2):
                num = num + 1
    return num 

if __name__ == "__main__":
    inputfile = open("C-small-attempt0.in",'r')
    outputfile = open('result1','w')
    num = int(inputfile.readline())
    for i in range(num):
        record = inputfile.readline()
        a = record.split(' ')[0]
        b = record.split(' ')[1]
        outputfile.write("Case #"+str(i+1)+': '+str(test(int(a),int(b)))+'\n')