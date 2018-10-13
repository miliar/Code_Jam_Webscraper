'''
The Next Number: Google Codejam 2009 Round 1b

Created on Sep 12, 2009

@author: Chris
'''
import sys

#From Michael Davies's recipe.
def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

# Taken from http://stackoverflow.com/questions/212358/binary-search-in-python
def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            #print "g"
            lo = mid+1
        elif midval > x: 
            #print "l"
            hi = mid
        else:
            #print "f"
            return mid
    return -1

file = open(sys.argv[1])

testCases = int(file.readline())
#print 'test cases: ' + str(testCases)

test = 1
while test <= testCases:
    number = file.readline().strip()
    #print 'Desired Number: ' + number
    #for char in number:
    #    print char + ' ',
    numbers = []

    for p in all_perms(list(number)):
        #print ''.join(p)
        numbers.append(int(''.join(p)))

    numbers.sort()
    
    hi = numbers[len(numbers)-1]
    
    last = numbers[-1]
    for i in range(len(numbers)-2, -1, -1):
       if last==numbers[i]: del numbers[i]
       else: last=numbers[i]
    
    #print numbers, hi
    #hi = int(number)
    
    # If number is max, append a zero and start again
    if int(number) == hi:
    #if index == len(numbers):
        numbers = []
        myList = list(number)#.append('0')
        myList.append('0')   
        for p in all_perms(myList):
            numbers.append(int(''.join(p)))
        
        numbers.sort()
        
        hi = numbers[len(numbers)-1]
        last = numbers[-1]
        for i in range(len(numbers)-2, -1, -1):
           if last==numbers[i]: del numbers[i]
           else: last=numbers[i]
        #print numbers, hi
    
    index = binary_search(numbers,int(number))
    
    if index != -1:
        #print index
       # try:
        print 'Case #' + str(test) + ': ' + str(numbers[index+1])
        #except IndexError:
            #print 'Case #' + str(test) + ': ' + str(numbers[index+1])
        
    
    
    
    test+=1
    
    
