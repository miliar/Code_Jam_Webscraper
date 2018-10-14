import fileinput
import psyco
psyco.full()

def addPath(p, existingDirs):
    accum = ""
    count = 0
    for x in p.split("/"):
        accum = accum + x + "/"
        if accum not in existingDirs:
            count += 1
        #print accum, existingDirs
        existingDirs.add(accum)
    return count


def handleCase(existingPathes,newPathes):
    existingDirs = set(["/"])
    #print existingPathes
    #print newPathes
    for x in existingPathes:
        addPath(x.strip(), existingDirs)
    count = 0
    for x in newPathes:
        count += addPath(x.strip(), existingDirs)
    return count

def main():
    it = fileinput.input()
    caseCount = int(it.next())
    for i,x in enumerate(it):
        (existingCount, newCount) = [int(y) for y in x.split()]
        existingPathes = []
        for j in range(existingCount):
            existingPathes.append(it.next())
        newPathes = []
        for j in range(newCount):
            newPathes.append(it.next())
        print "Case #%d: %d" % (i+1,handleCase(existingPathes,newPathes))

if __name__ == "__main__":
    main()
