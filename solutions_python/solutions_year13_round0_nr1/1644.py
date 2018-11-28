

def hasEmptyCell(Tlst):
    for row in Tlst:
        for elem in row:
            if elem == '.':
                return True
    return False

def ifRow(row):
    if row in ['XXXT','XXTX','XTXX','TXXX','XXXX']:
        return 1
    elif row in ['OOOT','OOTO','OTOO','TOOO','OOOO']:
        return 2
    else:
        return 0
    
def checkRow(Tlst):
    for row in Tlst:
        r = ifRow(row)
        if (r > 0):
            return r
    return 0

def checkCol(Tlst):
    for i in range(4):
        s = ''
        for j in range(4):
            c = Tlst[j][i]
            s+=c
        #print s
        r = ifRow(s)
        if (r > 0):
            return r
    return 0
    
def checkDiag(Tlst):
    s = ''
    for j in range(4):
        c = Tlst[j][j]
        s+=c
    #print s
    r = ifRow(s)
    if (r > 0):
        return r
    
    s = ''
    for j in range(4):
        c = Tlst[j][3-j]
        s+=c
    #print s
    r = ifRow(s)
    if (r > 0):
        return r
    
    return 0

def checkMap(Tlst):
    
    a = checkRow(Tlst)
    b = checkCol(Tlst)
    c = checkDiag(Tlst)
    
    l = [a,b,c]
    #print l
    if 1 in l:
        return 1
    if 2 in l:
        return 2
    return 0


def main():
    inpfile = open("A-large.in", 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line1 = inpfile.readline().strip()
        line2 = inpfile.readline().strip()
        line3 = inpfile.readline().strip()
        line4 = inpfile.readline().strip()
        inpfile.readline()
        S = ""
        
        listTotal = [line1, line2, line3, line4]

        #print listTotal

        #print hasEmptyCell(listTotal)
        
        #print checkRow(listTotal)
        #print checkCol(listTotal)
        #print checkDiag(listTotal)
        
        
        
        if hasEmptyCell(listTotal):
            
            x = checkMap(listTotal)
            if (x == 1):
                S = 'X won'
            if (x == 2):
                S = 'O won'
            if (x == 0):
                S = 'Game has not completed'
           
                
            
        else: # not empty
            x = checkMap(listTotal)
            if (x == 1):
                S = 'X won'
            if (x == 2):
                S = 'O won'
            if (x == 0):
                S = 'Draw'
            
        
        result = "Case #" + str(case) + ": " + str(S)+"\n"
        print result
        
        outfile.write(result)
    inpfile.close()
    outfile.close()




if __name__ == "__main__":


    main()
    

    
    