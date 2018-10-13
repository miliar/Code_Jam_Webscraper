infile = open("B-small-attempt0.in","r")
outfile = open("small_output.out","w")

numbCase = eval(infile.readline())
case = 0

def findTidy(int):
    lastDigit = 0
    count = 0
    int = str(int)
    lenInt = len(int)
    for i in range(0,lenInt):
        digit = eval(int[count])
        count += 1
        if digit >= lastDigit:
            lastDigit = digit
            if count == lenInt:
                return True
        else:
            return False

def main(case):
    for i in range(0,numbCase):
        int = eval(infile.readline())
        case += 1
        while True:
            if findTidy(int) == True:
                print("Case #", case, ": ", int, sep="", file=outfile)
                break
                
            else:
                int -= 1
    
lastTidy = main(case)
outfile.close()