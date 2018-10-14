#! /usr/bin/env python3.0

def replaceBlueWithRed(tab2):
    tab = []
    for s in tab2:
        tab.append(list(s))
    for num, ligne in enumerate(tab):
        for i in range(1, len(ligne)-1):
            # bad squares Horiz
            if ((ligne[i] == "#") and ((not ligne[i+1] == "#") and (not ligne[i-1] == "#"))):
                return "Impossible"
        
        if ((not ligne == tab[-1]) and (not ligne == tab[0])):
            for i in range(len(ligne)):
                # bad squares Vertic
                if ((ligne[i] == "#") and (not tab[num+1][i] == "#") and (not tab[num-1][i] == "#")):
                    return "Impossible"
    
    # Possible
    
    for numL in range(len(tab)):
        for numC in range(len(tab[numL])):
            if (not tab[numL][numC] == "#"):
                continue
            
            if (numL == 0): #first line
                if (numC == 0): # first col
                    tab[numL][numC] = "/" # top-left
                
                elif (tab[numL][numC-1] == "/"):
                    tab[numL][numC] = "\\" # top-right
                
                elif (tab[numL][numC-1] == "\\"):
                    tab[numL][numC] = "/" # top-left
                
                else:
                    tab[numL][numC] = "/"
            
            else: # others lines
                
                if (numC == 0): #first col
                    if (tab[numL-1][numC] == "/"):
                        tab[numL][numC] = "\\" # bottom-left
                    
                    else:
                        tab[numL][numC] = "/" # top-left
                
                else:
                    # other lines, other cols
                    
                    if (tab[numL-1][numC] == "/"):
                    
                        if (tab[numL-1][numC-1] == "."):
                            tab[numL][numC] = "\\"
                            
                        elif (tab[numL][numC-1] == "."):
                            
                            if (tab[numL-1][numC-1] == "/"):
                                tab[numL][numC] = "\\"
                            
                            elif (tab[numL-1][numC-1] == "\\"):
                                tab[numL][numC] = "/"
                        
                        elif (tab[numL][numC-1] == tab[numL-1][numC-1] == "\\"):
                            tab[numL][numC] = "/"
                        
                        
                        else:
                            tab[numL][numC] = "\\"
                        
                    elif (tab[numL-1][numC] == "\\"):
                    
                        if (tab[numL][numC-1] == "/"):
                            if (tab[numL-1][numC-1] == "/"):
                                tab[numL][numC] = "\\"
                            else:
                                if (tab[numL-1][numC-1] == "."):
                                    tab[numL][numC] = "\\"
                                else:
                                    tab[numL][numC] = "/"
                        
                        else:
                            tab[numL][numC] = "/"
                    
                    elif (tab[numL-1][numC] == "."):
                        if (not tab[numL-1][numC-1] == "."):
                        
                            if ((tab[numL][numC-1] == "/") and (not tab[numL-1][numC-1] == "\\")):
                                tab[numL][numC] = "\\"
                            else:
                                tab[numL][numC] = "/"
                        
                        elif (tab[numL][numC-1] == "\\"):
                            tab[numL][numC] = "/"
                          
                        
                        elif (tab[numL][numC-1] == "."):
                            tab[numL][numC] = "/"
                        
                        
                        elif (tab[numL][numC-1] == "/"):
                            tab[numL][numC] = "\\"
    tab3 = []
    for l in tab:
        tab3.append("".join(l))
    return printTab(tab3)

def countColor(color, tab):
    total = 0
    for ligne in tab:
        for li in ligne:
            if (li == color):
                total += 1
    return total

def printTab(tab):
    p = ""
    for i in tab:
        p += i + "\n"
    return p[:-1]

fic = input()

f = open(fic, "r")
lines = [li.replace("\n", "") for li in f.readlines()]
f.close()

T = int(lines[0])

lines = lines[1:]

f = open("output.txt", "w")

curseur = 0

for i in range(T):
    
    tab = []
    
    nbLines = int(lines[curseur].split(" ")[0])
    nbCols = int(lines[curseur].split(" ")[1])
    
    for j in range(nbLines):
        tab.append(lines[curseur+j+1])
    
    if (countColor("#", tab) == 0):
        retour = printTab(tab)
    
    elif (countColor("#", tab)%4 != 0):
        retour = "Impossible"
    
    else:
        retour = replaceBlueWithRed(tab)
    
    out = "Case #"+str(i+1)+":\n"+retour
    if (not i == T-1):
        out += "\n"
    print(out)
    f.write(out+"\n")
    
    curseur += nbLines+1

f.close()