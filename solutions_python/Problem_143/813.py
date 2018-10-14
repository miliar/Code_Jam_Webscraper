import sys;

if len(sys.argv) < 2:
    fileInput = sys.stdin;
    fileOutput = sys.stdout;

elif len(sys.argv) < 3:
    if (sys.argv[1][0] == "-"):
        fileInput = sys.stdin;
    else:
        fileInput = open(sys.argv[1], 'r');
        
    fileOutput = sys.stdout;

else:
    if (sys.argv[1][0] == "-"):
        fileInput = sys.stdin;
    else:
        fileInput = open(sys.argv[1], 'r');

    if (sys.argv[2][0] == "-"):
        fileOutput = sys.stdout;
    else:
        fileOutput = open(sys.argv[2], 'w');


flagDebug = False;
if (len(sys.argv) >= 4):
    if (sys.argv[3] == "-d"):
        flagDebug = True;

elif (len(sys.argv) == 3):
    if (sys.argv[2] == "-d"):
        flagDebug = True;

elif (len(sys.argv) == 2):
    if (sys.argv[1] == "-d"):
        flagDebug = True;

        
def debugPrint(strDebugMsg):
    global flagDebug;
    
    if (flagDebug):
        print (strDebugMsg);    

strTestcases = fileInput.readline();
nTestcases = int(strTestcases);

debugPrint("Found " + str(nTestcases) + " testcases.");

for i in range(nTestcases):
    debugPrint("");
    debugPrint("Case #" + str(i + 1));

    strInputLine = fileInput.readline().strip();
    lstInputLine = strInputLine.split(" ");

    (nA, nB, nK) = [int(x) for x in lstInputLine];

    debugPrint("A: %d, B: %d, K: %d" % (nA, nB, nK));

    if (nA > nK) and (nB > nK):
        nOutput = nB * nK;
        nOutput = nOutput + (nA - nK) * nK;

        for a in range(nK, nA):
            for b in range(nK, nB):
                if (a & b) < nK:
                    nOutput = nOutput + 1;
        
    else:
        nOutput = nB * nA;



    fileOutput.write("Case #%d: %d \n" % (i + 1, nOutput));
