import sys
import string
import is_palindrome_v1 as P
import math
def Compare(min,max):
    """ (int,int) -> int
    """
    count = 0;
    for num in range(min,max+1):
        flo = math.sqrt(num) - int(math.sqrt(num))
        #print (flo)
        if (flo == 0.0 and P.is_palindrome_v1(str(num))
            and P.is_palindrome_v1(str(int(math.sqrt(num))))):
            print (num)
            count = count + 1
    return count 

file = open("d:/C-small-attempt1.in", 'r')
out  = open("d:/test.out", 'w')
num_line = 1;
line = file.readline()  
line = line.rstrip('\n')
line = line.rstrip()
nums = line.split(' ')
n = nums[0];
for line in file:
    line = line.rstrip('\n')
    line = line.rstrip()
    nums = line.split(' ')
    min = (int)(nums[0])
    max = (int)(nums[1])
    count = Compare(min,max)
    print ("Case #" + str(num_line) +": " + str(count) + "\n")
    out.write("Case #" + str(num_line) +": " + str(count) + "\n")
    num_line = num_line + 1
                

   
    

file.close()
out.close()
