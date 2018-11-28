import sys;


if len(sys.argv) < 2:
    fileInput = sys.stdin;
    fileOutput = sys.stdout;

elif len(sys.argv) < 3:
    if (sys.argv[1] == "-"):
        fileInput = sys.stdin;
    else:
        fileInput = open(sys.argv[1], 'r');
        
    fileOutput = sys.stdout;

else:
    if (sys.argv[1] == "-"):
        fileInput = sys.stdin;
    else:
        fileInput = open(sys.argv[1], 'r');

    if (sys.argv[2] == "-"):
        fileOutput = sys.stdout;
    else:
        fileOutput = open(sys.argv[2], 'w');


flagDebug = False;
if (len(sys.argv) >= 4):
    if (sys.argv[3] == "-d"):
        flagDebug = True;


def debugPrint(strDebugMsg):
    global flagDebug;
    
    if (flagDebug):
        print (strDebugMsg);    

strTestcases = fileInput.readline();
nTestcases = int(strTestcases);

debugPrint("Found " + str(nTestcases) + " testcases.");
debugPrint("");

for i in range(nTestcases):
    rowFirst = int(fileInput.readline().strip()) - 1;

    lstRowsFirst = list();
    for j in range(0, 4):
        strLine = fileInput.readline();
        lstRowsFirst.append(strLine.split());

    rowSecond = int(fileInput.readline().strip()) - 1;

    lstRowsSecond = list();
    for j in range(0, 4):
        strLine = fileInput.readline();
        lstRowsSecond.append(strLine.split());

    lstCommon = list();
    for c in lstRowsFirst[rowFirst]:
        if c in lstRowsSecond[rowSecond]:
            lstCommon.append(c);

    if len(lstCommon) == 1:
        fileOutput.write("Case #" + str(i + 1) + ": " + str(lstCommon[0]) + "\n");
    elif len(lstCommon) == 0:
        fileOutput.write("Case #" + str(i + 1) + ": Volunteer cheated!\n");
    else:
        fileOutput.write("Case #" + str(i + 1) + ": Bad magician!\n");
