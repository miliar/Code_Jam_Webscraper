import sys
import os

MY_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
IN_LEN = 3
START_COOCKIE_SPEED = 2.0
OUT_STR = "Case #{}: {}\n"

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
            data = content[i].split(" ")
            factoryCost = float(data[0])
            factoryProd = float(data[1])
            winningSit = float(data[2])
            
            prevSolTime = 0.0
            prevStepTime = 0.0
            j = 0
            while(True):
                solTime = prevStepTime + (winningSit / (START_COOCKIE_SPEED + (j * factoryProd)))
                factProdTime = factoryCost / (START_COOCKIE_SPEED + (j * factoryProd))
                if (j != 0) & (solTime > prevSolTime):
                    break
                prevSolTime = solTime
                prevStepTime += factProdTime
                j += 1
            f.write(OUT_STR.format(i, "{0:.7f}".format(prevSolTime)))
                
             
            
