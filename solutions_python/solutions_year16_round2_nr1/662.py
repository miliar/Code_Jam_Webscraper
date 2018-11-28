def runCases(fname,outname):
    case = 0
    with open(fname,'rU') as f:
        for line in f:
            if case == 0: 
                cases = int(line)
                case+=1
                continue
            if case > cases: break
            ans = findPhoneNumber(line)
            outputCase(ans,outname,case)
            case+=1

def outputCase(ans,outname,case):
    if case == 1: f = open(outname,'w')
    else: f = open(outname,'a')
    f.write("Case #"+str(case)+": "+str(ans)+"\n")
    
def findPhoneNumber(line):
    chars = list(line)
    phoneNumber = []
    for d in [0,6,8,4,5,2,7,3,1,9]:
        numberInList = True
        while numberInList:
            try: 
                removeDigit(chars,d)
                phoneNumber.append(d)
            except ValueError:
                numberInList = False
    s = ""
    for d in sorted(phoneNumber):
        s += str(d)
    return s
                
def removeDigit(chars,d):
    if d == 0:
        chars.remove("Z")
        chars.remove("E")
        chars.remove("R")
        chars.remove("O")
    elif d == 1:
        chars.remove("O")
        chars.remove("N")
        chars.remove("E")
    elif d == 2:
        chars.remove("W")
        chars.remove("T")
        chars.remove("O")
    elif d == 3:
        chars.remove("T")
        chars.remove("H")
        chars.remove("R")
        chars.remove("E")
        chars.remove("E")
    elif d == 4:
        chars.remove("U")
        chars.remove("F")
        chars.remove("O")
        chars.remove("R")
    elif d == 5:
        chars.remove("F")
        chars.remove("I")
        chars.remove("V")
        chars.remove("E")
    elif d == 6:
        chars.remove("X")
        chars.remove("I")
        chars.remove("S")
    elif d == 7:
        chars.remove("V")
        chars.remove("S")
        chars.remove("E")
        chars.remove("E")
        chars.remove("N")
    elif d == 8:
        chars.remove("G")
        chars.remove("E")
        chars.remove("I")
        chars.remove("H")
        chars.remove("T")
    elif d == 9:
        chars.remove("N")
        chars.remove("I")
        chars.remove("N")
        chars.remove("E")
        
runCases("A-large.in","A-large.out")

    