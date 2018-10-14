def get_winner_from_row(row):
    size=len(row)
    o=0
    x=0
    for i in row:
        if i == 'X':
            x=x+1
        elif i == 'O':
            o=o+1
        elif i == 'T':
            o=o+1
            x=x+1
    if o == size:
        return 'O'
    if x == size:
        return 'X'
    return None

def column(matrix, i):
    return [row[i] for row in matrix] 
    

def get_result(matrix):
    size=len(matrix)
    rows=[]
    for i in range(0,size):
        rows.append(matrix[i])
         
    for i in range(0,size):
        col=column(matrix,i)
        rows.append(col)
        
    diagonal1=[]
    diagonal2=[]
    for i in range(0,size):
        diagonal1.append(matrix[i][i])
        diagonal2.append(matrix[i][size-i-1])
    rows.append(diagonal1)
    rows.append(diagonal2)
    for row in rows:
        winner=get_winner_from_row(row)
        if winner != None:
            return "{0} won".format(winner)
    for row in rows:
        if '.' in row:
            return 'Game has not completed'
    return 'Draw'
        

t=input()
for i in range(0,t):
    matrix=[]
    for j in range(0,4):        
        matrix.append(list(raw_input()))
    print "Case #{0}: {1}".format(i+1,get_result(matrix))    
    raw_input()
    
    