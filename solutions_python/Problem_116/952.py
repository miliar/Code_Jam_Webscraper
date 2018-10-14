import numpy as np
import sys

rpl = {
       ".":0,
       "X":3,
       "O":2,
       "T":1
       }

with open(sys.argv[2], "w") as outfile:
    with open(sys.argv[1], "r") as infile:
        game_count = int(infile.readline())
        for i in range(game_count):
            tmp =[]
            for j in range(4):
                line=infile.readline()[:-1]
                #print line, [rpl[c] for c in line]
                tmp.append([rpl[c] for c in line])
                # read
            infile.readline() # empty line
            game = np.array(tmp)
            g_res="D"
            g_com=True
            for g in (game, game.T, (game.diagonal(), (game[0,3], game[1,2], game[2,1], game[3,0]))):
                for line in g:
                    res=np.product(line)
                    if res:
                        if (res%3) and not (res%2):
                            g_res="O"
                            break
                        elif (res%2) and not (res%3):
                            g_res="X"
                            break
                    else:
                        g_com=False
                if not (g_res=="D"):
                    break
            if g_res=="D":
                if g_com==True:
                    outfile.write("Case #%d: Draw\n" % (i+1,))
                else:
                    outfile.write("Case #%d: Game has not completed\n" % (i+1,))
            else:
                outfile.write("Case #%d: %s won\n" % (i+1,g_res))
            