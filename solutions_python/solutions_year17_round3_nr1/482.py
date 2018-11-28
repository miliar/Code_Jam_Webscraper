
import math

def solve(n,k,sizeTpl):
    ByRadii = sorted(sizeTpl, key=lambda x: x[0])
    ByCSA = sorted(sizeTpl, key=lambda x: x[1])
    result = 0
    for i in range(k):
        result += ByCSA[-(i+1)][1]
    leftover = ByCSA[:-k]
    leastSA = ByCSA[-k]
    chosenByRad = sorted(ByCSA[-k:], key=lambda x: x[0])
    largest = chosenByRad[-1]
    top = math.pi*(largest[0]**2)
    leftBySA = sorted(leftover, key=lambda x: x[1]+math.pi*x[0]**2)
    try:
        contender = leftBySA[-1]
        if contender[1]+math.pi*(contender[0]**2) - top > leastSA[1]:
            result += (contender[1]+math.pi*(contender[0]**2))
            result -= leastSA[1]
        else:
            result+=top
    except:
        result += top
    return result



TestCases = int(input(""))
number = 0
for i in range(TestCases):
    number+=1
    line = input("")
    Parts = line.split(" ")
    n = int(Parts[0])
    k = int(Parts[1])
    sizeTpls = []
    for j in range(n):
        lines = input("")
        part = lines.split(" ")
        sizeTpls.append([float(part[0]),2*math.pi*float(part[0])*float(part[1])]) #rad, cylSA
    result = solve(n,k,sizeTpls)
    print("CASE #" + str(number) + ": " + str(result))
