import sys
import math

def process_file(inputFile):
    f = open(inputFile, 'r')
    numCases = int(f.readline())

    if numCases < 1:
        sys.stderr.write("Number of cases invalid\n")
        return False
    
    for x in xrange(numCases):
        fairAndSquareNums = 0
        line = f.readline()
        if line != '':
            (beginStr, endStr) = line.split()
        begin = int(beginStr)
        end = int(endStr)

        if begin < 1:
            sys.stderr.write("Invalid input: Beginning of range is invalid.\n")
            return False
        if end > 10**100:
            sys.stderr.write("Invalid input: End of range is invalid.\n")
            return False
        if begin > end:
            sys.stderr.write("Invalid input: Beginning of range is greater than end.\n")
            return False

        for num in xrange(begin,end+1):
            if is_palindrome(num) and math.sqrt(num).is_integer() and is_palindrome(int(math.sqrt(num))):
                fairAndSquareNums+=1

        sys.stdout.write("Case #%d: %d\n" % (x+1, fairAndSquareNums))
                
    f.close()

def is_palindrome(num):
    s = str(num)
    length = len(str(s))
    for x in xrange(length/2):
        if s[x] != s[length-x-1]:
            return False
    return True

if __name__ == "__main__":    
    process_file(sys.argv[1])
