import sys

def checkString(length, repeat, string):
    newString = ''
    for count in range(repeat):
        newString += string

    sign1 = 1
    product1 = '1'
    charCount = length * repeat
    signs1 = [1] * charCount
    products1 = ['1'] * charCount
    for sep1 in range(1, charCount - 1):
        (sign1, product1) = multiply(sign1, product1, newString[sep1 - 1])
        signs1[sep1] = sign1
        products1[sep1] = product1
    
    sign3 = -1
    product3 = '1'
    for sep2 in range(len(newString) - 1, 1, -1):
##        print "multiply3(%d, %s, %s)" % (sign3, product3, newString[sep2])
        (sign3, product3) = multiply(sign3, product3, newString[sep2])
        sign3 *= -1
##        print "result3(%d, %s)" % (sign3, product3)
        if sign3 != 1 or product3 != 'k':
            continue

        sign2 = -1
        product2 = '1'
        for sep1 in range(sep2 - 1, 0, -1):
##            print "multiply2(%d, %s, %s)" % (sign2, product2, newString[sep1])
            (sign2, product2) = multiply(sign2, product2, newString[sep1])
            sign2 *= -1
##            print "result2(%d, %s)" % (sign2, product2)
            if sign2 != 1 or product2 != 'j':
                continue

##            print "result1(%d, %s)" % (signs1[sep1], products1[sep1])
            if signs1[sep1] != 1 or products1[sep1] != 'i':
                continue

            return 'YES'
    return 'NO'

def checkStringSegments(string, sep1, sep2):
##    print "checkStringSegments(%s, %d, %d)" % (string, sep1, sep2)
    print "checkStringSegments(%d, %d)" % (sep1, sep2)
##    (sign, product) = checkStringSegment(string, 0, sep1)
##    print "sign=%d, product=%s" % (sign, product)
##    if sign != 1 or product != 'i':
##        return False
    
    (sign, product) = checkStringSegment(string, sep1, sep2)
##    print "sign=%d, product=%s" % (sign, product)
    if sign != 1 or product != 'j':
        return False
    
##    (sign, product) = checkStringSegment(string, sep2, len(string))
##    print "sign=%d, product=%s" % (sign, product)
##    if sign != 1 or product != 'k':
##        return False

    return True

def checkStringSegment(string, start, end):
##    print "checkStringSegment(%s, %d, %d)" % (string, start, end)
    reducedString = string
    sign = 1
##    reducedString = ''
##    index = start
##    while index + 1 < end:
##        if string[index] == string[index + 1]:
##            sign *= -1
##            index += 1
##        else:
##            reducedString += string[index]
##        index += 1
##    if index < end:
##        reducedString += string[end - 1]

##    print "reducedString: %s" % reducedString
##    if len(reducedString) == 0:
##        return (sign, '1')
    
    product = reducedString[0]
    for index in range(1, len(reducedString)):
        (sign, product) = multiply(sign, product, reducedString[index])
    return (sign, product)
        
def multiply(sign, char1, char2):
    if char1 == '1':
        if char2 == 'i':
            return ( 1 * sign, 'i')
        elif char2 == 'j':
            return ( 1 * sign, 'j')
        elif char2 == 'k':
            return ( 1 * sign, 'k')
    elif char1 == 'i':
        if char2 == 'i':
            return (-1 * sign, '1')
        elif char2 == 'j':
            return ( 1 * sign, 'k')
        elif char2 == 'k':
            return (-1 * sign, 'j')
    elif char1 == 'j':
        if char2 == 'i':
            return (-1 * sign, 'k')
        elif char2 == 'j':
            return (-1 * sign, '1')
        elif char2 == 'k':
            return ( 1 * sign, 'i')
    elif char1 == 'k':
        if char2 == 'i':
            return ( 1 * sign, 'j')
        elif char2 == 'j':
            return (-1 * sign, 'i')
        elif char2 == 'k':
            return (-1 * sign, '1')
    
def main():
    inFilename = sys.argv[1]
    outFilename = sys.argv[2]

    inFile = open(inFilename, 'r')
    outFile = open(outFilename, 'w')
    line = inFile.readline().rstrip()
    testCaseCount = int(line)
    for testCase in range(1, testCaseCount + 1):
        print "Test case %d:" % testCase
        line = inFile.readline().rstrip()
        data = line.split(' ')
        length = int(data[0])
        repeat = int(data[1])
        
        string = inFile.readline().rstrip()
        
        result = checkString(length, repeat, string)
        outFile.write("Case #%d: %s\n" % (testCase, result))
##        if testCase == 4:
##            break
    inFile.close()
    outFile.close()

if __name__ == '__main__':
    main()
