#!/usr/bin/python
import math

# read the test cases
f = open("input.txt", "r")
content = f.readlines()
f.close()

# define the variables
cases_count = 0
cases_low = []
cases_high = []
cases_result = []

# process the test cases into the variables
for line in content:
    if cases_count == 0:
        cases_count = int(line)
    else:
        tmp = line.replace("\n", "")
        tmp = tmp.split(" ")
        
        cases_low.append(int(tmp[0]))
        cases_high.append(int(tmp[1]))
        
# do the job
for i in range(0, cases_count):
    count = 0
    
    for x in range(cases_low[i], cases_high[i] + 1):
        palindrome = False
        squareofpalindrome = False
        
        converted = str(x)
        converted_reversed = converted[::-1]
        
        if converted == converted_reversed:
            palindrome = True
            
        squareof = str(math.sqrt(x))
        squareof = squareof.split(".")
        
        squareof_reversed = squareof[0][::-1]
        
        if squareof[0] == squareof_reversed:
            if squareof[1] == "0":
                squareofpalindrome = True
            
        if palindrome:
            if squareofpalindrome:
                count = count + 1
        
    cases_result.append(count)
    
# output the result
output = ""
for i in range(1, cases_count + 1):
    output = output + "Case #" + str(i) + ": " + str(cases_result[i - 1]) + "\n"
    
# save the output to a file
f = open("output.txt", "w")
f.write(output)
f.close()