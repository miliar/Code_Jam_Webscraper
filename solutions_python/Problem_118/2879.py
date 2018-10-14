
def isFair(s):
    """ determine if n is a palindrome """
    if len(s) <= 1:
         return True
    else:
        return s[0] == s[-1] and isFair(s[1:-1])
        
def isSquare(n):
    for i in range(1, n+1):
        #print i
        if i * i == n:
            return i
    return 0


f = open("C-small-attempt0.in.txt", "r")
numTest=f.readline()
#print numTest
case = 1
for line in f:
    line.rsplit()
    fairAndSquareCount = 0
    x, y = line.split(" ")
    for z in range(int(x), int(y)+1):
       if isFair(str(z)):
           #print str(z) + " is fair"
           root = isSquare(z)
           #print str(root)
           if root != 0 and isFair(str(root)):
              fairAndSquareCount += 1
    print "Case #" + str(case) + ": " + str(fairAndSquareCount)
    case +=1    
             
      
   
