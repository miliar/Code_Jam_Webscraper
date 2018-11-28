
import sys

inp = sys.argv[1]

f = open (inp, 'r')

lines = f.readlines()

testnums = lines[0]

tictacto = []

def diagnols (tictacto):
    pos1 = 0
    pos2 = 3
    diag1 = ""
    diag2 = ""
    for line in tictacto:
        diag1 = diag1 + line[pos1]
        diag2 = diag2 + line[pos2]
        pos1 += 1
        pos2 -= 1
    return (diag1, diag2)

def vertical (tictacto):
    res = ["","","",""]
    pos = 0
    for i in range(0,4):
        for line in tictacto:
            res[i] += line[i]
    
    return res

def test(tictacto):
    print "tictac:"
    print tictacto
    
    vert = vertical(tictacto)
    print "verticals", vert
    diag1,diag2= diagnols(tictacto)
    lines_to_chack = []
    lines_to_chack = tictacto
    lines_to_chack.append(diag1)
    lines_to_chack.append(diag2)
   # print "DIAG1:", diag1 
   # print "DIAG2:", diag2
    
    lines_to_chack = lines_to_chack + vert 
    print "lines_to_chack:", lines_to_chack
    for line in lines_to_chack:
        print "l:", line
        if("." not in line):
            line = line.replace("T", "")
            first = line[0]
            if(first == "X"):
                if ("O" not in line):
                    return "X won"
            else:
                if ("X" not in line):
                    return "O won"

    for line in tictacto:
        if ("." in line):
            return "Game has not completed"
    return "Draw"
            

            
        
    

case = 1
results = open ("results.txt", "w")
l = int(lines[0])
lines.append("")
for line in lines[1:]:
#    print line
    if case > l :
        exit(0)
    if line == "" or (len(tictacto) == 4):
        
        s = "Case #" + str(case)+ ": "+ test(tictacto)
        print s
        results.write(s + "\n") 
        case += 1
        tictacto = []
    else:
        tictacto.append(line)

results.close()
