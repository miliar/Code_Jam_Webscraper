import os
import math
import time

def isPalindrome(num):
    str_num = str(num)
    if str_num == str_num[::-1]:
        return True
    else:
        return False

def getPalindromeCount(A, B):
    M = int(math.ceil(math.sqrt(B)))
    m = 1
    count = 0
    for i in range(m,M-m+2):
        if isPalindrome(i):
            t = i*i;
            if t>=A and t<=B and isPalindrome(t):
                count += 1
    return count
    
if __name__=='__main__':
    filename = 'C-small-attempt0.in'
    
    f = open(filename)
    numbers = []
    case_size = -1
    result = []
    for line in f:
        if case_size < 0:
            case_size = int(line)
            continue
        
        ll = line.strip().split()
        if len(ll)<2:
            print 'wrong in format split'
            break
        if len(ll) == 2:
            numbers = [0]*2
            numbers[0] = int(ll[0])
            numbers[1] = int(ll[1])
        else:
            for i in range(0,len(ll)):
                try:
                    t = int(ll[i])
                    numbers.append(t)
                except:
                    continue
        if len(numbers)!=2:
            print 'wrong in input!'
            break
        A = min(numbers[0],numbers[1])
        B = max(numbers[0],numbers[1])
        c = getPalindromeCount(A, B)
        result.append(c)

    f.close()    
    
    resultFile = open('result2_small.txt','w')
    for i in range(0,len(result)):
        s = 'Case #'+str(i+1)+': '+ str(result[i]) + os.linesep
        resultFile.write(s)
    resultFile.close()
    
    end = time.time()