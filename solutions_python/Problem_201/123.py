import sys, copy;


def split2Intervals(n):
    if n % 2 == 0:
        return [n/2,n/2-1];
    else:
        return [n/2,n/2];
    
def divide(n):
    if n % 2 == 0:
        return str(n/2) + " " + str(n/2-1);
    else:
        return str(n/2) + " " + str(n/2);
def solve(n,k):
    #print "n",n,"k",k;
    if n == k:
        return "0 0"
    if k == 1:
        return divide(n);
    if k == 2:
        return divide(n/2);
    if k == 3:
        return divide(n/2 - 1 if n % 2 == 0 else n/2 )

    #intervals = [n];
    intervalsRanks = {n:1};
    i = 0;
    while i < k:
        """m = max(intervals);
        i+=1;
        intervals.remove(m);
        intervals += split2Intervals(m);"""
        
        m = max(intervalsRanks.keys());
        counts = intervalsRanks[m];
        i+=counts;
        del intervalsRanks[m];
        #intervalsRanks.removeKey(m);
        newIntervals = split2Intervals(m);
        if newIntervals[0] in intervalsRanks.keys():
            intervalsRanks[newIntervals[0]] += counts;
        else:
            intervalsRanks[newIntervals[0]] = counts;
        if newIntervals[1] in intervalsRanks.keys():
            intervalsRanks[newIntervals[1]] += counts;
        else:
            intervalsRanks[newIntervals[1]] = counts;
        
        #print "m:",m;
        
        
        
    return divide(m);

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print(inputFile, outputFile)
file = open(outputFile, "w")

with open(inputFile, 'r') as f:
    t = int(f.readline())
    print(t)
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": ")
        n,k=map(int,f.readline().split(" "))
        file.write(str(solve(n,k)) + "\n")
file.close()            








