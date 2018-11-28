#Problem A
f = open("A-small-attempt0.in");

def readProblem():
    prob = []
    prob.append( f.readline().strip('\n') )
    prob.append( f.readline().strip('\n') )
    prob.append( f.readline().strip('\n') )
    prob.append( f.readline().strip('\n') )
    return prob

def checkRow( row ):
    D = row.count('.');
    if D > 0:
        return (0,0,1)
    
    T = row.count('T');
    X = row.count('X') + T;    
    O = row.count('O') + T;

    return (X == 4 and 1 or 0, O == 4 and 1 or 0, 0)

def checkCol( prob, col ):
    C = prob[0][col] + prob[1][col] + prob[2][col] + prob[3][col]
    return checkRow( C )
    
def checkCross1( prob ):
    C = prob[0][0] + prob[1][1] + prob[2][2] + prob[3][3]
    return checkRow( C )

def checkCross2( prob ):
    C = prob[0][3] + prob[1][2] + prob[2][1] + prob[3][0] 
    return checkRow( C )
    
def processProblem( prob , case):
    pointsX = 0
    pointsY = 0
    blanks = 0

    for i in range(4):
        (x, y, blank) = checkRow( prob[i] )
        blanks += blank
        pointsX += x
        pointsY += y
        #print("POINTS: " + str(pointsX) + str(pointsY)) 
        
        (x, y, blank) = checkCol( prob, i )
        blanks += blank
        pointsX += x
        pointsY += y
        #print("POINTS Col: " + str(pointsX) + str(pointsY)) 
        
    (x, y, blank) = checkCross1( prob )
    blanks += blank
    pointsX += x;
    pointsY += y;
    #print("POINTS: " + str(pointsX) + str(pointsY)) 
    
    (x, y, blank) = checkCross2( prob )
    blanks += blank
    pointsX += x;
    pointsY += y;

    #print("POINTS: " + str(pointsX) + str(pointsY)) 
    
    if pointsX == pointsY:
        if blank > 0:
            print(case + "Game has not completed")
        else:
            print(case + "Draw");
        
    elif pointsX > pointsY:
        print(case + "X won");
    else:
        print(case + "O won")
        

    
problems = int(f.readline())

for i in range(problems):
    prob = readProblem()
    case = "Case #" + str(i + 1) + ": "
    processProblem( prob, case)
    f.readline()
    
f.close();
