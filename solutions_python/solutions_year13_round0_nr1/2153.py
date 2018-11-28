def check_row_win(row):
    if(row==[] or '.' in row):
        return False, None
    x = list(set(row))
    if(len(x)==1):
        return True, (x[0]+' won')
    elif (len(x)==2) and ('T' in x):
        x.remove('T')
        return True, (x[0]+' won')
    return False, None

def check_column_win(col):
    return check_row_win(col)

def check_diagonal_win(matrix):
    if matrix==[]:
        return False, None
    x = [matrix[i][j] for i in xrange(4) for j in xrange(4) if i==j]
    flag, result = check_row_win(x)
    if(flag == False):
        x = [matrix[i][j] for i in xrange(4) for j in xrange(4) if i==3-j]
        flag, result = check_row_win(x)
    return flag, result

def check_for_dot(matrix):
    if matrix==[]:
        return 'Game has not completed'
    for i in range(4):
        if('.' in matrix[i]):
            return 'Game has not completed'
    return 'Draw'

ip = open("A-large.in", "r")
op = open("output.txt", "w")
t = int(ip.readline())
for i in xrange(t):
    row = []
    flag = False
    for j in xrange(4):
        lister = list(ip.readline().strip())
        if not flag:
            flag, result = check_row_win(lister)
        row += [lister]
    for j in xrange(4):
        if not flag:
            m = [row[x][j] for x in xrange(4)]
            flag, result = check_column_win(m)
    if not flag:
        flag, result = check_diagonal_win(row)
    if not flag:
        result = check_for_dot(row)
    op.write('Case #'+str(i+1)+': '+result+'\n')
    ip.readline()
ip.close()
op.close()
