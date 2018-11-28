#!/usr/bin/python2.6 -tt
import sys
sys.setrecursionlimit(1000000)
def openFile(path, right):
    file = open(path, right)
    return file
    
def closeFile(file):
    file.close()    

def solve(farmPrice, rate, goal, t, coockieBought):
    timeToGoal = goal * (1/t)
    timeToBigCoockie = farmPrice * (1/t)
    tooMuchAlready = goal <= coockieBought + farmPrice
    tooLong =  timeToGoal <  timeToBigCoockie + (goal / (t + rate))
    
    #print(str(coockieBought + farmPrice + farmPrice))
    if tooMuchAlready or tooLong:
        # print("ttg " + str(timeToGoal))
        #print(str(coockieBought))
        return timeToGoal
    else:
        nr = t + rate
        ab = coockieBought + farmPrice
        #print("ttc " + str(timeToBigCoockie))
        return timeToBigCoockie + solve(farmPrice, rate, goal, nr, ab)

def main():
    path = "source.in"
    output = "output"
    file = openFile(path, "rU")
    outputFile = openFile(output, "wb")
    
    for i in range(int(next(file))):
        outputFile.write(str("Case #" + str( i + 1 ) + ": "))
        variables = map(float, next(file).split())
        c = float(variables[0])
        f = float(variables[1])
        x = float(variables[2])
        outputFile.write(str("{0:.7f}".format(solve(c, f, x, 2.0, 0.0))))
        outputFile.write("\n");
        #print("----------------------------------------------")
    
    closeFile(file)
    closeFile(outputFile)
	
#launch the main function
if __name__ == '__main__':
	main()