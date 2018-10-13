# Qualification Round 2012
# C. Recycled Numbers
# Roman Stolper (romocop)

# imports
import sys;
import string;

def main():
    # get input filename from command line args
    if (len(sys.argv) != 2):
        print "Must specify input file!";
        return 1;

    inputFile = str(sys.argv[1]);
    outputFile = inputFile + ".out";
        
    # open input file
    f_in = open(inputFile, 'r');
    f_out = open(outputFile, 'w');
    
    runTests(f_in, f_out);

    f_in.close();
    f_out.close();

def runTests(f_in, f_out):
    numTests = int(f_in.readline());
    for i in range(0, numTests):
        runTest(f_in, f_out, i+1);

def runTest(f_in, f_out, testNum):
    line = f_in.readline();
    (a, b) = parseLine(line);
    numPairs = countRecycledPairs(a, b);
    result = str(numPairs);
    print "Test #" + str(testNum);
    #print "Line: " + line + "Result: " + result;
    f_out.write("Case #" + str(testNum) + ": " + result + "\n");
    
def parseLine(line):
    pieces = string.split(line);
    a = int(pieces[0]);
    b = int(pieces[1]);
    return (a, b);
    
# loop n from A to B (inclusive of B)
# for each n, look at all the "recyclings" of it, and if a recycling
# is larger than n and less than B, increment numPairs
def countRecycledPairs(a, b):
    numPairs = 0;
    for n in range(a, b+1):
        nStr = str(n);
        mSet = set();
        for i in range(1, len(nStr)):
            m = int(nStr[i::] + nStr[0:i:]);
            if (m > n and m <= b and m not in mSet):
                #print "n: "+str(n)+", m: " + str(m);
                numPairs += 1;
                mSet.add(m)
    return numPairs;
main();