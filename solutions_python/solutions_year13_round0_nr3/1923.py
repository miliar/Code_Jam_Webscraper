import math
def findFandS(A, B):
    def isPalindrome(x):
        strNum = str(x)
        reverseStrNum = strNum[::-1]
        return strNum == reverseStrNum
       
    
    highestNum = int(math.sqrt(B))
    lowestNum = int(math.sqrt(A))
    if (lowestNum**2 != A):
       lowestNum = int(lowestNum)+1

    rtRange = range(lowestNum, highestNum+1)

    
    
    palindromes = filter(isPalindrome, rtRange)
   
    squares = map(lambda x: x**2,palindromes)

    fairAndSquare = filter(isPalindrome, squares)
    

    count = len(fairAndSquare)

    return count





FILENAME = "C-small-attempt0"
f = open(FILENAME + '.in', 'r')
N = int(f.readline())
output = []
for i in range(N):
    temp = f.readline().split(' ')
    A = int(temp[0])
    B = int(temp[1])
   
    output += ["Case #"+str(i+1)+": " + str(findFandS(A, B))]


f.close()
output = '\n'.join(e for e in output)
f = open(FILENAME + '.out', 'w')
f.write(output)
f.close()
