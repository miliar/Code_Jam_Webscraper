'''
Created on 14/04/2013

@author: Adam
'''
# Naive approach for quick points because running out of time
import math
infile = open('qc_input_easy.txt', 'r')
cases = int(infile.readline())
results = []
for case in range(0,cases):
    count = 0
    ab = infile.readline().split(' ')
    a = int(ab[0])
    b = int(ab[1])
    for num in range(a, b+1):
        val = str(num)
        if val == val[::-1]: # Palindrome!
            root = int(math.sqrt(int(val)))
            if root * root == num: # We have a whole-number sqrt...
                if str(root) == str(root)[::-1]:
                    count += 1
    results.append(count)
    
outfile = open('output.txt', 'w')
count = 0
for result in results:
    count += 1 
    outfile.write('Case #' + str(count) + ': ' + str(result) + '\n')

infile.close()    
outfile.close()


                
            
            