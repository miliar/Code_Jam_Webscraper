T = int(input())

# takes a string, Returns an integer..
def fix(myNumber):
    #Take previous as the starting character...
    prev = int(myNumber[0])
    for i in range(0,len(myNumber)):
        curr = int(myNumber[i])
        if prev > curr:
            #print('fixing '+myNumber)
            left = str(int(myNumber[:i])-1) #slice string till (but not including) current character and subtract 1 from the resultant number
            #eg. 123108---> left = 123-1 = 122
            nRight = len(myNumber[i:]) #Digits on the right
            right = '9'*nRight # if there wer 3 digits to right eg. 123108, then left = 122 right = 999 and
            tidy = int(left + right)
            #print('fixed'+str(tidy))
            break
        else:
            prev = curr
    return tidy

#takes a string, returns a boolean..
def isNonDecreasing(myNumber):
    prev = myNumber[0]
    for ch in myNumber:
        if int(prev) > int(ch):
            #print("*******Ooopss...Case #{}: {} : {}".format(t+1,number,stidy))
            return False
        prev = ch
    return True


for t in range(0,T):
    number = int(input())
    stringNumber = str(number)
    N = len(stringNumber)
    if N>1:
        while not isNonDecreasing(stringNumber):
            tidy = fix(stringNumber)
            stringNumber = str(tidy)
    # for single digit, input = output.
    else:
        stringNumber =  str(number)    
    finalNumber = stringNumber
    if not isNonDecreasing(finalNumber):
        print("Oops...Case #{}: Original->{} : Output->{}".format(t+1,number,finalNumber))
    print("Case #{}: {}".format(t+1, finalNumber))
