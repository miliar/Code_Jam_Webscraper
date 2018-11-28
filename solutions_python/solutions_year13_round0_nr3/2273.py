import math

def ispalindrome(number):
    strnumber=str(number)
    invstrnumber=strnumber[::-1]
    if strnumber == invstrnumber:
        return True
    else:
        return False
    
def fairandsquare(number):
    fnumber2=math.sqrt(number)
    if fnumber2.is_integer():
        number2=int(fnumber2)
        if ispalindrome(number) and ispalindrome(number2):
            return True
    return False


lines = open("file2.txt").readlines()
del lines[0]
i=0
for line in lines:
    npals = 0
    limits = line.split()
    for n in range(int(limits[0]),int(limits[1])+1):
        if fairandsquare(n): npals = npals + 1
    i = i + 1 
    print "Case #"+str(i)+": "+str(npals)
