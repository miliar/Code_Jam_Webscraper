import sys

def findResult(C, F, X, R, accum):
    if (X-C)/R <= X/(R+F):
        return accum + X/R
    else:
        return findResult(C, F, X, R+F, accum+(C/R))

if __name__ == '__main__':
    fileInput = open(sys.argv[1], 'r')
    fileOutput = open("output.txt", 'w')

    numCases = int(fileInput.readline())

    for case in range(numCases):
        print("Case #"+str(case+1)+":")
        fileOutput.write("Case #"+str(case+1)+":")

        temp = [float(x) for x in fileInput.readline().split()]
        C = temp[0] #Cost to building
        F = temp[1] #Extra cookie per building
        X = temp[2] #Exit term
        R = 2.0     #Rate of receving cookies
        accum = 0.0

        if X < C:
            fileOutput.write(" "+str(X/2.0))
        else:
            while (X-C)/R > X/(R+F):
                accum += (C/R)
                R += F
            accum += X/R
            
            fileOutput.write(" "+str(accum))
        if case < numCases-1:
            fileOutput.write("\n")

