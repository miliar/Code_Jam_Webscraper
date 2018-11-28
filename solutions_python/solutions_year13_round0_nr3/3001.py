import string
import math
import Queue

inputfilename = "C-small-attempt0.in"
inputfile = open(inputfilename, 'r')
outputfile = open("results.txt", 'w')

def testFNSq( val ):
    sqr_str = str(val*val)
    sqr_str_len = len(sqr_str)
    if sqr_str_len == 1:
        return 1
    if sqr_str_len%2 == 0:
        left = (sqr_str_len/2)-1
        right = (sqr_str_len/2)
    else:
        left = (sqr_str_len/2)-1
        right = (sqr_str_len/2)+1
    while(left >=0 and right <sqr_str_len):
        if(sqr_str[left] != sqr_str[right]):
            return 0
        left-= 1
        right+= 1
    return 1

        

def howMany(a, b):
    palindrome_staging = Queue.PriorityQueue()
    numFairNsquare = 0
    max_value = math.sqrt(b)
    for i in range( 1,10 ):
        if i <= max_value:
            palindrome_staging.put(i)
        if i+10*i <= max_value:
            palindrome_staging.put(i+10*i)

    current_val = palindrome_staging.get()
    current_val_string = str(current_val)
    if(current_val*current_val>=a):
        numFairNsquare = numFairNsquare + testFNSq(current_val)
    while (not palindrome_staging.empty()) and (int( str(1) + current_val_string + str(1)) <= max_value):
        for i in range( 1,10 ):
            next_val = int( str(i) + current_val_string + str(i))
            if next_val>=a and next_val <= max_value:
                palindrome_staging.put(next_val)
        current_val = palindrome_staging.get()
        current_val_string = str(current_val)
        if(current_val*current_val>=a):
            numFairNsquare = numFairNsquare + testFNSq(current_val)

    while not palindrome_staging.empty(): 
        current_val = palindrome_staging.get()
        if(current_val*current_val>=a):
            numFairNsquare = numFairNsquare + testFNSq(current_val)

    return numFairNsquare




num_tests = int(inputfile.readline());

for i in range(0,num_tests):
    test_line = inputfile.readline().split(' ')
    a = int(test_line[0])
    b = int(test_line[1])
    x = howMany(a,b)    
    outputfile.write("Case #%d: %d\n" %(i+1, x))

    
