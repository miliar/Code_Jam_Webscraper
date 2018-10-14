# Google Code Jam 2013
# Fair and Square
# Guilherme Rezende <guilhermebr@gmail.com>

def sqrta(x):
    ans = 0
    if x>=0:
        while ans*ans <x:
            ans = ans + 1
        if ans*ans == x:
            return ans
        
    return None    



def isPalindrome(x):    
    if x == x[::-1]:
        return True

    return False



#__main__
try:
    inFile = open('inputCsmall.txt', 'r')
    outFile = open('output.txt', 'w+')

    test_cases = inFile.readline()

    test_cases = int(test_cases.strip('\n'))

    for test in range(1, test_cases+1):
        line = inFile.readline().strip('\n')
        line = line.split()
        a = line[0]
        b = line[1]

        result = 0

        for c in range(int(a), int(b)+1):
            if isPalindrome(str(c)):
                x = sqrta(c)
                if x and isPalindrome(str(x)):
                    result += 1

        print 'Case #%d: %s' % (test, result)
        outFile.write('Case #%d: %s\n' % (test, result))

finally:
    inFile.close()
    outFile.close()