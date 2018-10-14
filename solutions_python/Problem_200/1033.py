import sys
import os, stat

def main():
    mode = os.fstat(0).st_mode
    input = None
    if stat.S_ISFIFO(mode):
        #print "stdin is piped"
        input = open("input.txt")
    elif stat.S_ISREG(mode):
        #print "stdin is redirected"
        input = sys.stdin
    else:
        #print "stdin is terminal"
        input = open("input.txt")

    numLines = int(input.readline())
    lines = (input.readline().rstrip('\n') for i in range(numLines))
    for (i,line) in enumerate(lines):
        print 'Case #%d: %s'%(i+1, str(evaluate(line)))

def evaluate(line):
    digits = [int(char) for char in line]
    def fix(digits, startIndex, endIndex):
        for i in range(startIndex, endIndex):
            if digits[i] > digits[i+1]:
                digits[i] -= 1
                digits[i+1:] = [9]*(len(digits)-(i+1))
                return i

    fixedIndex = fix(digits, 0, len(digits)-1)
    if (fixedIndex):
        for i in range(fixedIndex-1, -1, -1):
            fix(digits, i, i+1)
    return int(''.join(str(digit) for digit in digits))

main()

