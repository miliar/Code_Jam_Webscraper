# google code jam 2013 qualification round
# fair and square
# Written by mark grandi
# 04/13/2013
#

import sys, math

def solveProblem(filepath):
    ''' solves the problem'''

    numOfTests = 0
    testList = []
    # load the tests
    with open(filepath, "r", encoding="utf-8") as f:
        numOfTests = int(f.readline())

        for i in range(numOfTests):
            testList.append(f.readline().split(" "))

    with open("fair_and_square_output.txt", "w", encoding="utf=8") as output:

        # go through the tests
        for testNumber, entry in enumerate(testList, start=1):
            startNumber = int(entry[0])
            endNumber = int(entry[1])

            #print(startNumber, endNumber)

            output.write("Case #{}: ".format(testNumber))

            numberOfFairAndSquareNumbers = 0
            for tmpNumber in range(startNumber, endNumber +1):
                # fair and square number - it is a number that is a palindrome and the square of a palindrome 
                # at the same time. For instance, 1, 9 and 121 are fair and square (being palindromes and squares, 
                # respectively, of 1, 3 and 11), while 16, 22 and 676 are not fair and square: 16 is not a palindrome, 
                # 22 is not a square, and while 676 is a palindrome and a square number, it is the square of 26, which 
                # is not a palindrome. 

                numSqrt = math.sqrt(tmpNumber)

                # see if the number is a palindrome, a square (the square root times the square root equals the original number) and if the square
                # is a palindrome as well
                # see http://stackoverflow.com/questions/2489435/how-could-i-check-if-a-number-is-a-perfect-square?lq=1
                #import pdb;pdb.set_trace()
                if isPalindrome(tmpNumber) and ( (int(numSqrt + 0.5) ** 2) == tmpNumber) and isPalindrome(int(numSqrt)):
                    numberOfFairAndSquareNumbers +=1
                    #print(tmpNumber)
            output.write("{}\n".format(numberOfFairAndSquareNumbers))





def isPalindrome(num):
    ''' sees if a number is a plaindrome'''

    # only one digit numbers are always palindrome
    if num < 10:
        return True

    strNum = str(num)
    # even numbers
    if len(strNum) % 2 == 0:
        
        firstHalf = strNum[:int(len(strNum)/2)]
        secondHalf = strNum[int(len(strNum) /2):]

        secondHalf = reverseStr(secondHalf)

        return firstHalf == secondHalf

    # odd numbers
    if len(strNum) % 2 != 0:

        toCount = math.floor(len(strNum) / 2)

        firstHalf = strNum[:toCount]
        secondHalf = strNum[-toCount:]
        secondHalf = reverseStr(secondHalf)

        return firstHalf == secondHalf


def reverseStr(string):
    ''' reverses and returns a string'''
    finalStr = ""

    for x in range(len(string)):
        finalStr += string[-1]
        string = string[:-1]

    return finalStr





if len(sys.argv) < 2:
    print("need input!")
    sys.exit(1)

solveProblem(sys.argv[1])
