import sys
import math

#find the number of factories to get before going straight for the goal
def findNumFactories(c, f, x):
    #save time by using closed form solution
    return max(0, int(math.ceil(x/c - 2/f -1)))

#total time to win with the strategy to 
def totalTime(c, f, x, n):
    T = 0
    for i in range(n):
        T += c/(2 + i * f)
    T += x/(2 + n * f)
    return T

if __name__ == "__main__":
    inFile = open(sys.argv[1], "r")
    outFile = open(sys.argv[2],"w")
    numExamples = int(inFile.readline())
    for i in range(numExamples):
        outFile.write("Case #" + str(i + 1) + ": ")
        c, f, x = [float(num) for num in inFile.readline().split(" ")]
        T = totalTime(c, f, x, findNumFactories(c, f, x))
        outFile.write(str(T) + "\n")
    
    inFile.close()
    outFile.close()

        
