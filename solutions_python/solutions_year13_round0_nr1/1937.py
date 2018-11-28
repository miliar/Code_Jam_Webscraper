from numpy import multiply, product

global dic
dic = {"X": 2, "O": 3, "T":1, ".":0}

def get_board(lines):
    row_acc = []
    
    for k in range(4):
        l = []
        for i in range(4):
            l.append(dic[lines[k][i]])
        row_acc.append(l)
        
    col_acc = []
    
    for k in range(4):
        l = []
        for i in range(4):
            l.append(dic[lines[i][k]])
        col_acc.append(l)
    #print "Col_acc is", col_acc
    #print "Roc_acc is", row_acc
    return (row_acc, col_acc)

def solve(board):
    (row_acc, col_acc) = board
    contains_dot = False
    for i in range(4):
        s=product(row_acc[i])
        #print "Prod: ", s
        if s == 3**3 or s == 3**4:
            return "O won"
        elif s == 2**3 or s == 2**4:
            return "X won"
        elif  s== 0:
            contains_dot = True
    for j in range(4):
        s=product(col_acc[j])
        #print "Prod: ",s
        if s == 3**3 or s == 3**4:
            return "O won"
        elif s == 2**3 or s == 2**4:
            return "X won"
        elif s== 0:
            contains_dot = True

    dia1= row_acc[0][0]*row_acc[1][1]*row_acc[2][2]*row_acc[3][3]
    dia2= row_acc[3][0]*row_acc[2][1]*row_acc[1][2]*row_acc[0][3]
    
    if dia1 == 3**3 or dia1 == 3**4 or dia2 == 3**3 or dia2 == 3**4:
        return "O won"
    elif dia1 == 2**3 or dia1 == 2**4 or dia2 == 2**3 or dia2 == 2**4:
        return "X won"
    elif dia1== 0 or dia2==0:
        contains_dot = True

    
    if contains_dot:
        return "Game has not completed"
    else:
        return "Draw"
    
    
    
def tic_tac():
    inp = "A-large.in"
    out = "A-large.in-OUT.txt"
    f = open(inp, 'r')
    fo = open(out, 'w')
    num_lines = f.readline()
    for j in range(int(num_lines)):
        
        line1 = f.readline().replace("\n","")
        line2 = f.readline().replace("\n","")
        line3 = f.readline().replace("\n","")
        line4 = f.readline().replace("\n","")
        line5 = f.readline().replace("\n","")
        lines =[line1,line2,line3,line4]
        #print "The lines are ", lines
        b=get_board(lines)
        result = solve(b)
        print "Result is: ", result
        fo.write("Case #{0}: {1}".format(j+1,result))
           
        fo.write("\n")
tic_tac()
