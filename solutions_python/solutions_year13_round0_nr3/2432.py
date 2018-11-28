from math import sqrt

def find(first):
    first = first.split( )
    a = int(first[0])
    num = int(first[1])
    ans = 0
    
    while (num >= a):
        
        num_re = int(str(num)[::-1])
        
        if (num == num_re):      # check palindrome
            if (is_square(num)):    # check perfect square
                keep = int(num**0.5)     # keep squared number
                keep_re = int(str(keep)[::-1])
                
                if (keep == keep_re):      # check palindrome
                    ans+=1 
        num-=1
    return ans

def is_square(n):
    return sqrt(n).is_integer()


infile = open('C-small-attempt0.in','r') # open input file
output_file = open("output.txt", "w") # open output file

t = int(infile.readline())  # read number of test case

testcase = 1

for first in infile: # start from the second line
    output_file.write("Case #" + str(testcase) + ": " + str(find(first))+"\n")
    testcase+=1



infile.close() # close input file
output_file.close() # close output file
