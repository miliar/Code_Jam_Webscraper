import sys, copy, math;

def solve():
    c = '+'
    flips = 0;
    ss=list(s);
    for i in range(0,len(ss)):
        #print ss[i];
        x = ss[i];
        if x == c:
            continue;
        #print len(ss)-i, k;
        if len(ss)-i >= k:
            flips+=1;
            #print "flips: ", flips
            for j in range(0,k):
                #print ss[i+j];
                ss[i+j] = '-' if ss[i+j] == c else '+';
                #print ss[i+j];
        else:
            return "IMPOSSIBLE"
    return flips;
    
    

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print( inputFile, outputFile)
file = open(outputFile, "w")

with open(inputFile, 'r') as f:
    t = int(f.readline())
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": ")
        s,k = f.readline().split(" ")
        k = int(k)
        file.write(str(solve()) + "\n")
file.close()            








