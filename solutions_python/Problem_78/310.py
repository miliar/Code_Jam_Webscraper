input1 = open(r"c:\googlecode\A-small-attempt2.in")
#input1 = open(r"c:\googlecode\A-small.txt")
lines = input1.readline()
totalC= int(lines.strip('\n'))
case =1
output1 = open(r"c:\googlecode\Asmall2.txt", 'w')
def GCD (a, b):
    if b==0:
        return a
    return GCD (b, a%b)

def LCM(a, b):
    return a*(b/GCD(a, b))

def toInt(aList):
    temp = []
    for key in aList:
        temp.append(int(key))
    return temp

lines = input1.readline()
while lines !='':
    lines= lines.strip("\n")
    tempL = lines.split(' ')
    tempL = toInt(tempL)
    if tempL[1]!=100 and tempL[2]==100:
        result ='Broken'
    elif tempL[1] ==0:
        result = 'Possible'
    elif tempL[2] ==0 and tempL[1] !=0:
        result = 'Broken'
    else:
        x = LCM(100, tempL[1])
        if x/tempL[1] > tempL[0]:
            result ='Broken'
        else:
            y =LCM(100, tempL[2])
            if y/tempL[2] >= x/tempL[1]:
                result ='Possible'
            else:
                result ='Broken'
    out= "Case #"+str(case) +": "+result+ "\n"
    output1.write(out)
    case +=1
    lines = input1.readline()
output1.close()

input1.close()
