#Code jam template adapted from martin-thoma:
#https://martin-thoma.com/google-code-jam-templates/
#To run: pypy main.py < test.in > result.txt

def isNeat(num):
    strNum = str(num)
    lastDigit = None
    for c in reversed(strNum):
        if lastDigit != None:
            if lastDigit < int(c):
                return False
        lastDigit = int(c)
    return True

def solve(cipher):
    num = int(cipher)

    while isNeat(num) != True:
        powTen = 0
        for c in reversed(str(num)):
            if int(c) != 9:
                #Set the last non-9 digit to 9
                num -= (10 ** powTen) * (int(c) + 1)
                break
            powTen += 1

    return str(num)
    

if __name__ == "__main__":
    testcases = input()

    for caseN in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseN, solve(cipher)))