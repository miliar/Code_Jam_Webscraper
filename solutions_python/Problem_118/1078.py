import math

def read(f):
    line = f.readline()
    data = [int(i) for i in line.split()]
    return data 

def checkresult(input):
    start = math.sqrt(input[0])
    end = math.sqrt(input[1])
    counter = 0
    if start == int(start):
        counter += checkReverse(int(start))
    start = int(start)+1
    while start <= end:
        counter += checkReverse(start)
        start +=1
    return counter

def checkReverse(start):
    if str(start) == str(start)[::-1]:
        num = start*start
        numStr = str(num)
        if numStr == numStr[::-1]:
            return 1
        return 0    
    return 0
def main():
    f = open("input.txt")
    counter = int(f.readline())
    case = 1
    while case<= counter:
        result = checkresult(read(f))
        print "Case #%s: %s"%(case,result)
        case +=1
        
main()