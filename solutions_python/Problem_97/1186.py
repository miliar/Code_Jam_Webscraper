#-------------------------------------------------------------------------------
# Problem C. Recycled Numbers
#-------------------------------------------------------------------------------

def isRecycled(n,m):
    if (n>=m):
        return False

    ns = str(n)
    ms = str(m)

    if len(ns) != len(ms):
        return False

    for i in range(1,len(ns)):
        recycled = ns[i:] + ns[:i]
        if m == int(recycled):
            return True

    return False

def parseLine(line):
    values=line.split();
    A = int(values[0]);
    B = int(values[1]);

    return (A,B)

def calculate(A,B):
    count = 0
    for n in range(A,B+1):
        for m in range(n,B+1):
            if isRecycled(n,m):
                count+=1
    return count

def main():
    fd = open( "input.txt" )
    numoflines = int(fd.readline())
    count = 0;

    for i in range (1,numoflines+1):
        (A,B) = parseLine(fd.readline())
        result = calculate(A,B)
        print ("Case #%d: %d"%(i,result))
    pass

if __name__ == '__main__':
    main()