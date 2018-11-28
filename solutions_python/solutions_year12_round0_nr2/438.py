#default gcj in file reader
#Boreeas, 7/3/2012
fin = open("in")
fout = open("out", "w")
case = 0

def wrt(out):
    global case
    case += 1
    fout.write("Case #" + str(case) + ": " + str(out) + "\n")

def getCount(surprise, threshold, scores):
    count = 0
    for score in scores:
        if score < threshold:
            continue
        modScore = score
        modScore -= ((threshold*2)-1)
        if (modScore >= (threshold - 1)):
            count += 1
        elif (modScore >= (threshold - 3)) and surprise > 0:
            surprise -= 1
            count+= 1
    return count

fin.readline()  #skip number-of-cases
while 1:
    line = fin.readline().rstrip()
    if not line:
        break
    
    args = line.split(" ")
    numDancers = int(args[0])
    numSurprise = int(args[1])
    threshold = int(args[2])
    scores = [int(i) for i in args[3:]]
    wrt(getCount(numSurprise, threshold, scores))
#release handles
fin.close()
fout.close()
