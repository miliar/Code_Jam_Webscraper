import math

def isPalindrome(n):
    n = str(n)
    if len(n) < 2:
        return True
    if n[0] != n[-1]:
        return False
    return isPalindrome(n[1:-1])

inFileName = input()
outFileName = "result.out"

inFile = open(inFileName, 'r')
outFile = open(outFileName, 'w')

numTest = inFile.readline().strip()

print(numTest)

for i in range(int(numTest)):
    A, B = inFile.readline().strip().split(' ')
    A = int(A)
    B = int(B)

    count = 0
    for j in range(A, B + 1):
        if isPalindrome(j):
            sqrtJ = math.sqrt(j)
            if int(sqrtJ) == sqrtJ:
                if isPalindrome(int(sqrtJ)):
                    count = count + 1

    print(count)
    result = "Case #" + str(i + 1) + ": " + str(count)
    outFile.write(result + "\n")

inFile.close()
outFile.close()
