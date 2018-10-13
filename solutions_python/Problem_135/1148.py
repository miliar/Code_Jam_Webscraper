import sys
import os

MY_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
BAD_MAG_STR = "Bad magician!"
VOL_CHEAT_STR = "Volunteer cheated!"
IN_LEN = 3
OUT_STR = "Case #{}: {}\n"
IN_SIZE = 10

if len(sys.argv) != IN_LEN:
    print "Bad input len!"
else:
    ifile = sys.argv[1]
    ofile = sys.argv[2]

    with open(os.path.join(MY_FILE_PATH, ifile)) as f:
        content = f.readlines()

    with open(os.path.join(MY_FILE_PATH, ofile), "w") as f:
        problemSize = int(content[0])
        for i in range(0, problemSize):
            fcr = content[1 + int(content[1 + (i*IN_SIZE)]) + (i*IN_SIZE)].rstrip('\n').split(" ")
            scr = content[6 + int(content[6 + (i*IN_SIZE)]) + (i*IN_SIZE)].rstrip('\n').split(" ")
            common = filter(lambda x:x in fcr, scr)
            lenCommon = len(common)
            if lenCommon == 1:
                f.write(OUT_STR.format(i + 1, int(common[0])))
            elif lenCommon < 1:
                f.write(OUT_STR.format(i + 1, VOL_CHEAT_STR))
            elif lenCommon > 1:
                f.write(OUT_STR.format(i + 1, BAD_MAG_STR))
                
             
            
