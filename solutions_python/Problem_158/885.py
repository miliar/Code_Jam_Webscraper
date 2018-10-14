fname = "D-small-attempt3.in"

with open(fname) as f:
    content = f.readlines()
    N = int(content[0])
    content.pop(0)
    for caseNo in range(0,N):
        treasure = content[caseNo].split()
        treasure = list(map(int, treasure)) #convert to int
        
        x, r, c = treasure[0], treasure[1], treasure[2]
        toPrint = "Case #"+str(caseNo+1)+": "
        if((((x // (min([r,c])+1)) + (x % (min([r,c])+1))) > (min([r,c]))) or (x > max([r,c]))):
             toPrint += "RICHARD"
        elif(((r*c-x) % x) == 0):
            if((x // min([r,c])) == min([r,c]) and ((x -(x // min([r,c]))) > 1)):
                toPrint += "RICHARD"
            else:
                toPrint += "GABRIEL"
        else:
            toPrint += "RICHARD"
        print(toPrint)