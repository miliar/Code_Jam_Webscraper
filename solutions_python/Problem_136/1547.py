def calculateTime(c, f, w):
    t = 0
    n = 0
    ori = w
    while w > 0:
        dontAddFarm = t + ori / (2.0 + n*f)
        t += c/(2.0 + f*n)
        n += 1
        w  = w - c
        addFarm = t + ori / (2.0 + n*f)
##        print dontAddFarm, addFarm
        
        if (dontAddFarm)< (addFarm):
##            print "break", dontAddFarm, addFarm
            return dontAddFarm

    return addFarm


myfile = open("B-large.in.txt", "r")
output = open("output.txt", "w")

cases = int(myfile.readline().strip())
case = 0

while case < cases:
 
    [c, f,w]= (myfile.readline().split())
    answer = calculateTime(float(c), float(f), float(w))
    output.write("Case #"+ str(case+1) + ": " + str(answer) + "\n")
    case += 1

myfile.close()
output.close()

