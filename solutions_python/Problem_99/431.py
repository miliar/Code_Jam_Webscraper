# Round 1A 2012
# A. Password Problem
# Roman Stolper (romocop)

# imports
import sys;
import string;
import fractions;

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
    (a, b, P) = parseInput(f_in);
    expected = typePassword(a, b, P);
    result = "{0:.6f}".format(expected);
    result_out = "Case #" + str(testNum) + ": " + result + "\n";
    print result_out;
    f_out.write(result_out);
    
def parseInput(f_in):
    line = f_in.readline();
    pieces = string.split(line);
    a = int(pieces[0]);
    b = int(pieces[1]);
    line = f_in.readline();
    pieces = string.split(line);
    P = list();
    for i in range(0, len(pieces)):
        P.append(float(pieces[i]));
    return (a,b,P);
    
def typePassword(a,b,P):
    penaltyCost = b+1;
    optimalKeystrokes = penaltyCost + 1; # hit enter right away.. lets see if we can do btr
    # i = number of characters deleted
    for i in range(0, a):
        numKeystrokes = 2*i + (b-a) + 1; # num backspaces and retypes, num to finish, enter
        probSuccess = 1;
        for j in range(0, len(P) - i):
            probSuccess *= P[j];
        probFail = 1 - probSuccess;
        expectedKeystrokes = (numKeystrokes * probSuccess) + ((numKeystrokes + penaltyCost) * probFail);
        if (expectedKeystrokes < optimalKeystrokes):
            optimalKeystrokes = expectedKeystrokes;
    return optimalKeystrokes;
    
main();