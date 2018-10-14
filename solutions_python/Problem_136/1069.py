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
debugPrint("");

for i in range(nTestcases):
    strLine = fileInput.readline().strip();

    (strFarmCost, strFarmProduction, strTarget) = strLine.split();

    fltFarmCost = float(strFarmCost);
    fltFarmProduction = float(strFarmProduction);
    fltTarget = float(strTarget);

    debugPrint("Case #" + str(i + 1));
    debugPrint("\tC = " + str(fltFarmCost));
    debugPrint("\tF = " + str(fltFarmProduction));
    debugPrint("\tX = " + str(fltTarget));

    fltCookieProduction = 2.0;
    time = 0.0;
    while True:
        timeWithFarm = (fltFarmCost / fltCookieProduction) + (fltTarget / (fltCookieProduction + fltFarmProduction));
        timeWithoutFarm = fltTarget / fltCookieProduction;

        if timeWithoutFarm < timeWithFarm:
            time = time + timeWithoutFarm;
            break;

        time = time + fltFarmCost / fltCookieProduction;
        fltCookieProduction = fltCookieProduction + fltFarmProduction;

    strTime = "{:.7f}".format(time);

    fileOutput.write("Case #" + str(i + 1) + ": " + strTime + "\n");

    debugPrint("");
