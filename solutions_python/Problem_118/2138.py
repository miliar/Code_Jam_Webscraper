
import math

file = open("C-small-attempt0.in", 'r')

first = 0
cases = 0
case = 0
numrange = ""
count = 0

def is_palindrome(i):
    string = repr(i)
    reverse = string[::-1]
    #print string, reverse
    length = len(string)
    #if (length%2==0):#even
    string = string[0:length/2]
    reverse = reverse[0:length/2]
    if string == reverse:
        #print "TRUE!"
        return True
    else:
        #print "FALSE!"
        return False

for line in file:
    if (first == 0):
        first = 1
        cases = int(line)
    else:
        numrange = line.split(" ")
        numrange[0] = int(numrange[0])
        numrange[1] = int(numrange[1])
        count = 0
        for i in range(numrange[0], numrange[1]+1):
            if is_palindrome(i):
                #print i
                #if is_palindrome(math.sqrt(i)):
                sqrt = math.sqrt(i)
                if sqrt.is_integer():
                    if is_palindrome(int(sqrt)):
                        count += 1
        case += 1
        print "Case #"+repr(case)+": "+repr(count)

file.close()
