import math

def main():


    fout = open('problemCSmall.txt', 'w')
    fin = open('inputCSmall.in', 'r')

    testCases = fin.readline().strip()

    for i in range(int(testCases)):
        accumSum = 0
        ends = fin.readline().strip().split(" ")
        for j in range(int(ends[0]),int(ends[1])+1):
            
            issqrt, sqrt = isSqrt(j)
            if issqrt:
                if isPalindrome(j)==j:
                    if isPalindrome(sqrt)==sqrt:
                        accumSum = accumSum + 1

        fout.write("Case #" + str(i+1) + ": " + str(accumSum) + "\n")

def isPalindrome(num, partial=0):

    if num == 0:
        return partial
    return isPalindrome(num/10, partial *10+num%10)


def isSqrt(num):
    sqrt = int(math.sqrt(num))

    if sqrt*sqrt == num:
        return True, sqrt
    return False, sqrt

main()
