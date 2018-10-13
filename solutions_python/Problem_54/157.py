'''
Created on 8. svi. 2010.

@author: dpetek
'''


import sys

sys.stdout = open ( "B-large.out", "w")
fin = open ( "B-large.in")

n = int(fin.readline())


def gcd ( a, b):
    if b == 0 :
        return a
    return gcd ( b, a%b)

for test_case in range ( 1, n + 1):
    
    numbers = [int(num) for num in fin.readline().rstrip().split(" ")]
    numbers = numbers[1:]
    numbers.sort()
    
    if len(numbers) < 2 :
        print ("Case #%d: 0") % test_case
        break
    
    diffGCD = numbers[1]- numbers[0]
    
    for i in range ( 1, len(numbers)):
        for j in range ( 0, i):
            diffGCD = gcd ( diffGCD, numbers[i] - numbers[j])
    
    maxyIter = 0
    
    for i in range ( 1, len (numbers)):
        tmp = 0
        if numbers[i] % diffGCD == 0:
            tmp = 0
        else:
            tmp = (numbers[i] / diffGCD + 1) * diffGCD - numbers[i]
        if tmp > maxyIter:
            maxyIter = tmp
        
    print ("Case #%d: ") % test_case, maxyIter
        
sys.stdout = sys.__stdout__ 