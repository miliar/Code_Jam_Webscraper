numCases = int(raw_input())
import math
for n in range(numCases):
    case = raw_input().split()
    A,B = case
    A = int(A)
    B = int(B)
    
    def isPali(input):
            
        stack = []
        
        if len(input)%2 == 1:
            middle = (len(input)-1)/2
        else:
            middle = len(input)/2
            
        for char in input[:middle]:
            stack.append(char)
        if len(input)%2 == 1:
            middle = middle+1
        for char in input[middle:]:
            if stack.pop() != char:
                return False
        return True
        
    def isSquare(input):
        import math
        input = int(input)
        return math.sqrt(input)%1 == 0
        
    numFair = 0
    for i in range(A,B+1):
        if isPali(str(i)):
            if isSquare(i):
                temp = int(math.sqrt(i))
                
                if isPali(str(int(math.sqrt(i)))):
                    numFair += 1
    
    outputstring = str(numFair)
    print "Case #{0}: ".format(str(n+1)) + outputstring