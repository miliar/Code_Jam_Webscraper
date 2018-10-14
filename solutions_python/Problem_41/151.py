import sys

def main():   
    line = sys.stdin.readline().strip()
    values = line.split()

    testCaseCnt = int(values[0]);

    for testCaseNum in range(testCaseCnt):
        line = sys.stdin.readline().strip()
        digits = {}
        for i in range(10):
            digits[i] = 0
        for i in range(len(line)):
            digits[int(line[i])] += 1
        number = int(line)
        i = 1
        while True:
            if check(digits, number + i):
                break
            i = i + 1
        print 'Case #%d: %d' % (testCaseNum + 1, number + i)

def check(expectedDigits, number):
    actualDigits = {}
    for i in range(10):
        actualDigits[i] = 0
    while number > 0:
        digit = number % 10
        number = number / 10
        actualDigits[digit] += 1
        if digit <> 0 and actualDigits[digit] > expectedDigits[digit]:
            return False
    for i in range(10):
        if i <> 0 and actualDigits[i] <> expectedDigits[i]:
            return False
    return True    

if __name__ == "__main__":
    main()
