def x_win(elements):
    for i in range(4):
        win = True
        for j in range(4):
            if (elements[j][i] == 'X' or elements[j][i] == 'T') is False:
                win = False
                break
        if win is True:
            return True
    
    for i in range(4):
        win = True
        for j in range(4):
            if (elements[i][j] == 'X' or elements[i][j] == 'T') is False:
                win = False
                break
        if win is True:
            return True
        
    win = True
    for i in range(4):
        if (elements[i][i] == 'X' or elements[i][i] == 'T') is False:
            win = False
            break
    if win is True:
        return True
    
    win = True
    for i in range(4):
        if (elements[i][3-i] == 'X' or elements[i][3-i] == 'T') is False:
            win = False
            break
    if win is True:
        return True
    
    return False

def o_win(elements):
    for i in range(4):
        win = True
        for j in range(4):
            if (elements[j][i] == 'O' or elements[j][i] == 'T') is False:
                win = False
                break
        if win is True:
            return True
    
    for i in range(4):
        win = True
        for j in range(4):
            if (elements[i][j] == 'O' or elements[i][j] == 'T') is False:
                win = False
                break
        if win is True:
            return True
        
    win = True
    for i in range(4):
        if (elements[i][i] == 'O' or elements[i][i] == 'T') is False:
            win = False
            break
    if win is True:
        return True
    
    win = True
    for i in range(4):
        if (elements[i][3-i] == 'O' or elements[i][3-i] == 'T') is False:
            win = False
            break
    if win is True:
        return True
    
    return False

def is_completed(elements):
    for i in range(4):
        for j in range(4):
            if elements[i][j] == '.':
                return False
    return True

f = open('A-large.in', 'r')

set_count = int(f.readline())
results = []
for i in range(set_count):
    elements = [[0 for x in range(4)] for x in range(4)]
    for j in range(4):
        line = f.readline()
        for k in range(4):
            elements[k][j] = line[k]
    line = f.readline()
    
    if x_win(elements):
        results.append("Case #" + str(i+1) + ": X won")
    elif o_win(elements):
        results.append("Case #" + str(i+1) + ": O won")
    else:
        if is_completed(elements):
            results.append("Case #" + str(i+1) + ": Draw")
        else:
            results.append("Case #" + str(i+1) + ": Game has not completed")
    
    
f = open('A-large.out', 'w')            

for line in results:
    f.write(line + '\n')
print(set_count)