import math
def nextPalindrome(num):
    length=len(str(num))
    oddDigits=(length%2!=0)
    leftHalf=getLeftHalf(num)
    middle=getMiddle(num)
    if oddDigits:
        increment=pow(10, length/2)
        newNum=int(leftHalf+middle+leftHalf[::-1])
    else:
        increment=int(1.1*pow(10, length/2))
        newNum=int(leftHalf+leftHalf[::-1])
    if newNum>num:
        return newNum
    if middle!='9':
        return newNum+increment
    else:
        return nextPalindrome(roundUp(num))
 
def getLeftHalf(num):
    return str(num)[:len(str(num))/2]
 
def getMiddle(num):
    return str(num)[(len(str(num))-1)/2]
 
def roundUp(num):
    length=len(str(num))
    increment=pow(10,((length/2)+1))
    return ((num/increment)+1)*increment
def checkPalindrome(num):
    num=str(num)
    size=len(num)
    for i in range(0,size/2):
        if num[i] != num[size-i-1]:
            return False
    return True;
if __name__=="__main__":
    with open(r"c:\Users\user\Desktop\C-large-1.in") as inp_file:
        cases= int(inp_file.readline().strip())
        out_file=open(r"c:\Users\user\Desktop\fas.out","w")
        for i in range(1,cases+1):
            srange,erange=[int(x) for x in inp_file.readline().split()]
            sqrt=int(math.ceil(math.sqrt(srange)))
            sqrt=nextPalindrome(sqrt-1)
            num=sqrt**2
            fas=0
            while(num<=erange):
                if checkPalindrome(num):
                    fas+=1
                sqrt=nextPalindrome(sqrt)
                num=sqrt**2
            #print "Case #"+str(i)+": "+str(fas)
            out_file.write("Case #"+str(i)+": "+str(fas)+"\n")
        out_file.close()

