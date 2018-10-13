def isPalindrome(number):
    numString = str(number)
    palindrome = True;
    for i in range(len(numString)/2):
        if numString[i] != numString[-i-1]:
            palindrome = False
            break
        
    return palindrome

def fairSquare(number):
    if (isPalindrome(number) and isPalindrome(number**2)):
        return true
    return false;
    
def getCount(rangeStart, rangeEnd):
    import math
    count = 0
    start = int(math.ceil(math.sqrt(rangeStart)))
    end = int(math.floor(math.sqrt(rangeEnd)))
    for number in range(start,end+1):
        if isPalindrome(number) and isPalindrome(number**2):
            #print number**2
            count += 1

    return count

def main(filename):
    inputFile = open(filename,'r')
    line = inputFile.readline()
    cases = int(line[:-1])

    for i in range(cases):
        line = inputFile.readline()
        if i == cases-1:
            line = line + '\n'
        space = line.index(' ',1)
        start = int(line[:space])
        end = int(line[space+1:-1])
        
        counter = getCount(start,end)
        result = "Case #" + str(i+1) + ": " + str(counter)
        print result

filename = raw_input()
main(filename)
