#1. check for diagonal
def checkX():
    for j in range(2):
        winner = [None,0]
        for i in range(4):
            if j == 0:
                cell = table[i][i]
            elif j == 1:
                cell = table[i][3-i]

            if cell == ".":
                break
            
            if winner[0]:
                if winner[0] == cell:
                    winner[1] += 1
                elif cell == "T":
                    winner[1] += 1
                else:
                    break
            
            elif cell == "T":
                winner[1] += 1 
            
            else:
                winner[0] = cell
                winner[1] += 1 
        
        if winner[1] == 4:
            return "%s won" % winner[0]

def checkColums():
    for j in range(4):
        winner = [None,0]
        for i in range(4):
            
                
                cell = table[i][j]

                if cell == ".":
                    break
                
                if winner[0]:
                    if winner[0] == cell:
                        winner[1] += 1
                    elif cell == "T":
                        winner[1] += 1
                    else:
                        break
                
                elif cell == "T":
                    winner[1] += 1 
                
                else:
                    winner[0] = cell
                    winner[1] += 1 
        if winner[1] == 4:
            return "%s won" % winner[0]



def checkRows():
    unfinished = False
    for j in range(4):
        winner = [None,0]
        for i in range(4):
            
                
                cell = table[j][i]

                if cell == ".":
                    unfinished = True
                    break
                
                if winner[0]:
                    if winner[0] == cell:
                        winner[1] += 1
                    elif cell == "T":
                        winner[1] += 1
                    else:
                        break
                
                elif cell == "T":
                    winner[1] += 1 
                
                else:
                    winner[0] = cell
                    winner[1] += 1 
        if winner[1] == 4:
            return "%s won" % winner[0]
    if unfinished:
        return 0
# Qualification round
inp = open("input.txt")
outp = open("output.txt","w")

CASES = int(inp.readline())

for case in range(CASES):
    table = [None,None,None,None]
    result = "Draw"
    for i in range(4):
        table[i] = inp.readline()
    inp.readline()
    
    winner = checkX()
    if winner:    
        outp.write("Case #%s: %s\n" % (case+1,winner)) 
        continue
    
    winner = checkColums()
    if winner:    
        outp.write("Case #%s: %s\n" % (case+1,winner)) 
        continue
    
    winner = checkRows()
    if winner:    
        outp.write("Case #%s: %s\n" % (case+1,winner)) 
        continue
    elif winner == 0:
        result = "Game has not completed"
        
    outp.write("Case #%s: %s\n" % (case+1,result)) 
           
inp.close()
outp.close()