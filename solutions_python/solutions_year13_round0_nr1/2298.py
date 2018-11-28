#!/usr/bin/python
#My first python
import sys
with open('game.txt') as f:
    content = f.readlines()
content = map(lambda s: s.strip(), content)
content = filter(None, content)
count = 0
numy = 0
linenum = 0
Found = True
game = [[0 for x in xrange(4)] for x in xrange(4)] 
T=[]
for line in content:
    for x in range(4):
        game[numy][x] = line[x]
        if line[x] == 'T':
            T.append([numy,x])
    numy+=1
    linenum+=1
    if linenum == 4:
        #change T to X
        for t in T:
            y = t[0]
            x = t[1]
            game[y][x] = 'X'
        #check row
        for y in range(4):
            if game[y][0] == game[y][1] == game[y][2] == game[y][3] == 'X':
                count +=1
                sys.stdout.write("Case #%d: X won\n" % (count))
                Found = False
                break
        if Found:
        #check col
            for x in range(4):
                if game[0][x] == game[1][x] == game[2][x] == game[3][x] == 'X':
                    count +=1
                    sys.stdout.write("Case #%d: X won\n" % (count))
                    Found = False
                    break
            if Found:
                #check X
                if game[0][0] == game[1][1] == game[2][2] == game[3][3] == 'X':
                    count +=1
                    sys.stdout.write("Case #%d: X won\n" % (count))
                    Found = False
                elif game[0][3] == game[1][2] == game[2][1] == game[3][0] == 'X':
                    count +=1
                    sys.stdout.write("Case #%d: X won\n" % (count))
                    Found = False
            if Found:
                #change T to O
                for t in T:
                    y = t[0]
                    x = t[1]
                    game[y][x] = 'O'
                #check row
                if Found:
                    for y in range(4):
                        if game[y][0] == game[y][1] == game[y][2] == game[y][3] == 'O':
                            count +=1
                            sys.stdout.write("Case #%d: O won\n" % (count))
                            Found = False
                            break
                    #check col
                if Found:
                    for x in range(4):
                        if game[0][x] == game[1][x] == game[2][x] == game[3][x] == 'O':
                            count +=1
                            sys.stdout.write("Case #%d: O won\n" % (count))
                            Found = False
                            break
                    #check X
                if Found:
                    if game[0][0] == game[1][1] == game[2][2] == game[3][3] == 'O':
                        count +=1
                        sys.stdout.write("Case #%d: O won\n" % (count))
                        Found = False
                    elif game[0][3] == game[1][2] == game[2][1] == game[3][0] == 'O':
                        count +=1
                        sys.stdout.write("Case #%d: O won\n" % (count))
                        Found = False
                    #check Draw or not completed
                    if Found:
                        for y in range(4):
                            if Found:
                                for x in range(4):
                                    if game[y][x] == '.':
                                        count+=1
                                        sys.stdout.write("Case #%d: Game has not completed\n" % (count))
                                        Found = False
                                        break
                        if Found:
                            count+=1
                            sys.stdout.write("Case #%d: Draw\n" % (count))

        Found = True
        game = [[0 for x in xrange(4)] for x in xrange(4)] 
        T=[]
        linenum = 0
        numy = 0
