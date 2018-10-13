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

def playWar(Naomi, Ken):
    cpNaomi = Naomi.copy();
    cpKen = Ken.copy();

    cpNaomi.sort();
    cpKen.sort();

    wonNaomi = 0;
    for bNaomi in cpNaomi:
        bKenWins = False;
        
        for bKen in cpKen:
            if (bKen > bNaomi):
                bKenWins = True;
                cpKen.remove(bKen);
                break;

        if bKenWins:
            continue;
            
        cpKen.pop(0);
        wonNaomi = wonNaomi + 1;

    return wonNaomi;

def playDWar(Naomi, Ken, cntBlocks):
    cpNaomi = Naomi.copy();
    cpKen = Ken.copy();

    cpNaomi.sort();
    cpKen.sort();

    wonNaomi = 0;
    for i in range(cntBlocks):
        if cpNaomi[-1] > cpKen[0]:
            for bNaomi in cpNaomi:
                if bNaomi > cpKen[0]:
                    cpNaomi.remove(bNaomi);
                    break;

            cpKen.pop(0);
            wonNaomi = wonNaomi + 1;
        else:
            cpNaomi.pop(0);
            cpKen.pop();
    
    return wonNaomi;

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
    strBlocks = fileInput.readline().strip();
    cntBlocks = int(strBlocks);

    strBlocksNaomi = fileInput.readline().strip();
    lstBlocksNaomi = strBlocksNaomi.split();
    lstBlocksNaomi = [float(b) for b in lstBlocksNaomi];

    strBlocksKen = fileInput.readline().strip();
    lstBlocksKen = strBlocksKen.split();
    lstBlocksKen = [float(b) for b in lstBlocksKen];

    assert(len(lstBlocksNaomi) == cntBlocks);
    assert(len(lstBlocksKen) == cntBlocks);
    
    winsWithWar = playWar(lstBlocksNaomi, lstBlocksKen);
    winsWithDWar = playDWar(lstBlocksNaomi, lstBlocksKen, cntBlocks);

    debugPrint("Wins though war: " + str(winsWithWar));
    debugPrint("Wins though dwar: " + str(winsWithDWar));

    fileOutput.write("Case #" + str(i + 1) + ": " + str(winsWithDWar) + " " + str(winsWithWar) + "\n");
