import math
import sys

sys.setrecursionlimit(10000)
def sevenFloat(f):
    return float(str("%0.7f" % f))

def cookieClick(cps,currsec,c,f,x):
    if c >= x:
        return x / cps
    else:
        timeToFarm = sevenFloat(c / cps)
        timeToFinish = sevenFloat(x / cps)
        timeToFinishWithFarm = sevenFloat(x / (cps + f))
        totalBuild = sevenFloat(timeToFarm + timeToFinishWithFarm)
        if (totalBuild < timeToFinish):
            #print("Building Farm")
            #print(str(cps+f) + " " + str(currsec + timeToFarm))
            return cookieClick(cps+f,currsec+timeToFarm,c,f,x)
        else:
            #print("Waiting Out...")
            currsec += timeToFinish
            return currsec
    

infile = open('B-small-attempt6.in', 'r')
outfile = open('B-small-out6.txt', 'w')

cases = int(infile.readline())
for i in range(1, cases+1):
    #print(str(i) + ": ")
    line = infile.readline().split()
    c = float(line[0])
    #print(c)
    f = float(line[1])
    #print(f)
    x = float(line[2])
    #print(x)
    ans = cookieClick(2.0,0.0,c,f,x)
    #print(ans)
    outfile.write("Case #" + str(i) + ": " + str(ans) + "\n")

infile.close()
outfile.close()
