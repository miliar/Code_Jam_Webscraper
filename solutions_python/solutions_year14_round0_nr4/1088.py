import sys
import os

MY_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
IN_LEN = 3
IN_SIZE = 3
OUT_STR = "Case #{}: {} {}\n"

def naomi_cheat_score(naomiList, kenList):
    if naomiList[0] > kenList[0]:
        del naomiList[0]
        del kenList[0]
        return 1
    else:
        del naomiList[len(naomiList)-1]
        del kenList[0]
        return 0

if len(sys.argv) != IN_LEN:
    print "Bad input len!"
else:
    ifile = sys.argv[1]
    ofile = sys.argv[2]

    with open(os.path.join(MY_FILE_PATH, ifile)) as f:
        content = f.readlines()

    with open(os.path.join(MY_FILE_PATH, ofile), "w") as f:
        problemSize = int(content[0])
        for i in range(1, problemSize + 1):
            kenBlocks = []
            naomiBlocks = []
            normalScore = 0
            cheatingScore = 0
            
            temp =  content[1 + ((i-1) * IN_SIZE) + 1].split(" ")
            for num in temp:
                naomiBlocks += [float(num)]
            temp =  content[1 + ((i-1) * IN_SIZE) + 2].split(" ")
            for num in temp:
                kenBlocks += [float(num)]
            
            kenBlocks.sort()
            naomiBlocks.sort()
            
            normalScore = len(kenBlocks)
            tempKen = list(kenBlocks)
            for j in range(0, len(naomiBlocks)):
                try:
                    del tempKen[next(x[0] for x in enumerate(tempKen) if x[1] > naomiBlocks[j])]
                    normalScore -= 1
                except:
                    pass
            
            kenBlocks = kenBlocks[::-1]
            naomiBlocks = naomiBlocks[::-1]
            
            while len(naomiBlocks) > 0:
                cheatingScore += naomi_cheat_score(naomiBlocks, kenBlocks)

            f.write(OUT_STR.format(i, cheatingScore, normalScore))
