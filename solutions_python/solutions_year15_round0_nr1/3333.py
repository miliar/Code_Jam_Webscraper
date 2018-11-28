def addPeople(maxShy,sequence):
    totalAdd = 0
    cumSum = 0
    for i in range(int(maxShy)+1):
        toAdd = max(0,i-cumSum)
        totalAdd += toAdd
        cumSum += toAdd + int(sequence[i])

    return totalAdd

def printOut(case,total,outObj):
    #print("Case #%d: %d"%(case,total))
    outObj.write("Case #%d: %d\n"%(case,total))

##################################

if __name__ == "__main__":

    file="A-large.in"
    outfile="ovation_large_submit.txt"
    f = open(file)
    out = open(outfile,'w')
    cases = int(f.readline().rstrip())
    for case in range(1,cases+1):
        maxShy,seq = f.readline().rstrip().split()
        printOut(case,addPeople(maxShy,seq),out)

    f.close()
    out.close()
