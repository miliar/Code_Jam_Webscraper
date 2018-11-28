inp=raw_input()

games=inp.split("\n")

cases=int(games[0])

games.remove(games[0])

while "" in games:
    games.remove("")
    
for c in range(0,cases):
    game=[["","","",""],["","","",""],["","","",""],["","","",""]]
    for i in range(4):
        for j in range(4):
            game[i][j]=games[c*4+i][j]
         
    for i in range(4):
        t=False
        if "X" in game[i] or "T" in game[i]:
            if "O" not in game[i] and "." not in game[i]:
                t=True
                break

    if t:
        print "Case #"+str(c+1)+": X won"

    else:    
        for i in range(4):
            t=False
            if "O" in game[i] or "T" in game[i]:
                if "X" not in game[i] and "." not in game[i]:
                    t=True
                    break

        if t:
            print "Case #"+str(c+1)+": O won"

        else:
            game=[["","","",""],["","","",""],["","","",""],["","","",""]]
            for i in range(4):
                for j in range(4):
                    game[j][i]=games[c*4+i][j]

            for i in range(4):
                t=False
                if "X" in game[i] or "T" in game[i]:
                    if "O" not in game[i] and "." not in game[i]:
                        t=True
                        break

            if t:
                print "Case #"+str(c+1)+": X won"

            else:    
                for i in range(4):
                    t=False
                    if "O" in game[i] or "T" in game[i]:
                        if "X" not in game[i] and "." not in game[i]:
                            t=True
                            break

                if t:
                     print "Case #"+str(c+1)+": O won"

                else:
                    for i in range(4):
                        t=True
                        if game[i][i]=="O" or game[i][i]==".":
                            t=False
                            break

                    if t:
                        print "Case #"+str(c+1)+": X won"

                    else:
                        for i in range(4):
                            t=True
                            if game[i][i]=="X" or game[i][i]==".":
                                t=False
                                break

                        if t:
                            print "Case #"+str(c+1)+": O won"

                        else:
                            for i in range(4):
                                t=True
                                if game[i][3-i]=="X" or game[i][3-i]==".":
                                    t=False
                                    break

                            if t:
                                print "Case #"+str(c+1)+": O won"

                            else:
                                for i in range(4):
                                    t=True
                                    if game[i][3-i]=="O" or game[i][3-i]==".":
                                        t=False
                                        break

                                if t:
                                    print "Case #"+str(c+1)+": X won"

                                else:
                                    t=False
                                    for i in range(4):
                                        if "." in game[i]:
                                            t=True
                                            break

                                    if t:
                                        print "Case #"+str(c+1)+": Game has not completed"
                                    else:
                                        print "Case #"+str(c+1)+": Draw"
