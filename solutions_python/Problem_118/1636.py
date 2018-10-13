# https://code.google.com/codejam/contest/2270488/dashboard#s=p2
import sys
import math

def readline():
    return sys.stdin.readline().rstrip()

def isPalindrome(num):
    nums = str(num)
    if nums == nums[::-1]:
        return True
    return False

def countFairAndSquare(start, end):
    count = 0
    start0 = int(math.ceil(math.sqrt(start)))
    end0 = int(math.floor(math.sqrt(end)))
    num = start0
    while num <= end0:
        if isPalindrome(num):
            if isPalindrome(num*num):
                count += 1
        num += 1
    return count

def generateFairAndSquare(start, end):
    fairAndSquare = []
    start0 = int(math.ceil(math.sqrt(start)))
    end0 = int(math.floor(math.sqrt(end)))
    num = start0
    while num <= end0:
        if isPalindrome(num):
            num2 = num*num
            if isPalindrome(num2):
                fairAndSquare.append(num2)
        num += 1
    return fairAndSquare

def countFairAndSquare2(start, end, fairAndSquare):
    start0 = -1
    end0 = -1
    for i in range(len(fairAndSquare)):
        if start0 < 0 and fairAndSquare[i] >= start:
            start0 = i
        if end0 < 0 and fairAndSquare[i] > end:
            end0 = i
    if end0 == -1:
        end0 = len(fairAndSquare)
    if start0 == -1:
        if start > fairAndSquare[len(fairAndSquare)-1]:
            start0 = len(fairAndSquare)
    #print start, end, ":", start0, end0
    return end0 - start0

t = int(readline())
fairAndSquare = generateFairAndSquare(1,10**14)
for x in range(t):
    line = readline()
    (start, end) = [int(s) for s in line.split()]
    p = countFairAndSquare2(start, end, fairAndSquare)
    #p = countFairAndSquare(start, end)
    print 'Case #{0:d}: {1:d}'.format(x+1, p)
 
