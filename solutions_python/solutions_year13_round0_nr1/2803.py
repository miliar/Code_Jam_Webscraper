#! /usr/bin/env python3.2
import sys;
import re;
def testcase(testnumber,case):
    winner = testwinner(case)
    #veo si el juego esta completo o incompleto
    if testcompleted(case):
        if winner == None:
            print("Case #" + str(testnumber) + ": Draw")
        else:
            print("Case #" + str(testnumber) + ": " + winner + " won")
    else:
        if winner == None:
            print("Case #" + str(testnumber) + ": Game has not completed")
        else:
            print("Case #" + str(testnumber) + ": " + winner + " won")
        

def testcompleted(case):
    for i in range(4):
        for j in range(4):
            if case[i][j] == ".":
                return 0
    return 1

def testwinner(case):
    #chequeo columnas
    for j in range(4):
        column = case[0][j] + case[1][j] + case[2][j] + case[3][j]
        if(re.match("TX{3}|X{3}T|X{4}",column)):
            return "X"
        elif(re.match("TO{3}|O{3}T|O{4}",column)):
            return "O"
    #chequeo filas
    for i in range(4):
        row = case[i][0] + case[i][1] + case[i][2] + case[i][3] 
        if(re.match("TX{3}|X{3}T|X{4}",row)):
            return "X"
        elif(re.match("TO{3}|O{3}T|O{4}",row)):
            return "O"
    #chequeo diagonales
    diagonal1 = case[0][0] + case[1][1] + case[2][2] + case[3][3]
    diagonal2 = case[0][3] + case[1][2] + case[2][1] + case[3][0]

    if(re.match("TX{3}|X{3}T|X{4}",diagonal1) or re.match("TX{3}|X{3}T|X{4}",diagonal2)):
        return "X"
    elif(re.match("TO{3}|O{3}T|O{4}",diagonal1) or re.match("TO{3}|O{3}T|O{4}",diagonal2)):
        return "O"
    
    return None
    
if(len(sys.argv) > 1):
    namefile = sys.argv[1]
    file = open(namefile, mode='r')
    testcases = int(file.readline())
    case = [[],[],[],[]]
    rows = []
    for t in range(testcases):
        rows = []
        rows.append(file.readline().replace('\n',''))
        rows.append(file.readline().replace('\n',''))
        rows.append(file.readline().replace('\n',''))
        rows.append(file.readline().replace('\n',''))
        for i in range(4):
            case[i].append(rows[i][0])
            case[i].append(rows[i][1])
            case[i].append(rows[i][2])
            case[i].append(rows[i][3])           
        file.readline()
        
        testcase(t+1,case)
        #despues de que lo testeo lo limpio
        case = [[],[],[],[]]
else:
    print("You must give me a input file")


