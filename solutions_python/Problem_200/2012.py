import sys
import math

def Problem2(num, n):
    numStr = str(n)
    while (True):
        digits = list(numStr)
        
        # find index where digit (index) is greater than digit (index+1)
        index = findIndex(digits)
        if index == -1:
            break;        
        
        numb = int(digits[index] + digits[index+1]);
        while (True):
            # find the first tidy 2-digit number
            numb = numb - 1;
            if math.floor(numb / 10) <= numb % 10:
                break
        
        # substitute 2 digits, then he rest by 9s
        digits[index] = str(math.floor(numb / 10));
        digits[index+1] = str(numb % 10);
        for i in range(index+2, len(digits)):
            digits[i] = '9'
        numStr = ''.join(digits)
    
    print("Case #" + str(num) + ": " + str(int(numStr)))


def findIndex(digits):
    for i in range (0, len(digits)-1):
        if (int(digits[i]) > int(digits[i+1])):
            return i
    return -1;



cnt = 0
numCases = 0
for line in sys.stdin:
    if cnt == 0:
        numCases = int(line)
    else:
        if cnt <= numCases:
            split = line.split()
            Problem2(cnt, int(line))
        else:
            break
        
    cnt = cnt + 1


    
