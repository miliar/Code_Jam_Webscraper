inFile = open('A-small-attempt2.in', 'r')
lines = inFile.readlines()
kupka = open('rizalts.txt', 'w')
print lines
x = 1
trial = 1
for i in range(int(lines[0])):
    plansza = [[], [], [], []]
    for j in range(4):
        plansza[j].append(lines[x][0])
        plansza[j].append(lines[x][1])
        plansza[j].append(lines[x][2])
        plansza[j].append(lines[x][3])
        x+=1
    x+=1
    a = 'X'
    b = 'O'
    result = None
    for line in plansza:
        for char in line:
            if char == '.':
                result = 'Case #' + str(trial) + ': Game has not completed'
                break
    for poziomo in range(4):
        if (plansza[poziomo][0] == a or plansza[poziomo][0] == 'T') and (plansza[poziomo][1] == a or plansza[poziomo][1] == 'T')\
           and (plansza[poziomo][2] == a or plansza[poziomo][2] == 'T') and (plansza[poziomo][3] == a or plansza[poziomo][3] == 'T'):
            result = 'Case #' + str(trial) + ': ' + a + ' won'
    for poziomo in range(4):
        if (plansza[poziomo][0] == b or plansza[poziomo][0] == 'T') and (plansza[poziomo][1] == b or plansza[poziomo][1] == 'T')\
           and (plansza[poziomo][2] == b or plansza[poziomo][2] == 'T') and (plansza[poziomo][3] == b or plansza[poziomo][3] == 'T'):
            result = 'Case #' + str(trial) + ': ' + b + ' won'
    for pionowo in range(4):
        if (plansza[0][pionowo] == a or plansza[0][pionowo] == 'T') and (plansza[1][pionowo] == a or plansza[1][pionowo] == 'T')\
           and (plansza[2][pionowo] == a or plansza[2][pionowo] == 'T') and (plansza[3][pionowo] == a or plansza[3][pionowo] == 'T'):
            result = 'Case #' + str(trial) + ': ' + a + ' won'
    for pionowo in range(4):
        if (plansza[0][pionowo] == b or plansza[0][pionowo] == 'T') and (plansza[1][pionowo] == b or plansza[1][pionowo] == 'T')\
           and (plansza[2][pionowo] == b or plansza[2][pionowo] == 'T') and (plansza[3][pionowo] == b or plansza[3][pionowo] == 'T'):
            result = 'Case #' + str(trial) + ': ' + b + ' won'
    if (plansza[0][0] == a or plansza[0][0] == 'T') and (plansza[1][1] == a or plansza[1][1] == 'T') and (plansza[2][2] == a or plansza[2][2] == 'T')\
       and (plansza[3][3] == a or plansza[3][3] == 'T'):
        result = 'Case #' + str(trial) + ': ' + a + ' won'
    if (plansza[0][0] == b or plansza[0][0] == 'T') and (plansza[1][1] == b or plansza[1][1] == 'T') and (plansza[2][2] == b or plansza[2][2] == 'T')\
       and (plansza[3][3] == b or plansza[3][3] == 'T'):
        result = 'Case #' + str(trial) + ': ' + b + ' won'
    
    if result == None:
        result = 'Case #' + str(trial) + ': Draw'
    trial += 1
    print result
    kupka.write(result+'\n')
    kupka.flush()
            
    
    
        
    print plansza
kupka.close()

