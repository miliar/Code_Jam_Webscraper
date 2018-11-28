# Qualification Round 2012
# A. Speaking in Tongues
# Roman Stolper (romocop)

# imports
import sys;
import string;

# make a translation table from Googlerese to regular text
# based on the string provided in the sample input
# as well as the "y qee" to "a zoo"
# as well as the missing translation of z->q
tab = string.maketrans('zy qeeejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv', 'qa zooour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up');

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
    result = string.translate(line, tab);# translate line via translation table;
    #print "Line: " + line + "Result: " + result;
    f_out.write("Case #" + str(testNum) + ": " + result);

main();