def xort(char):
    if char == 'X' or char == 'T':
        return 1
    return 0
    
def oort(char):
    if char == 'O' or char == 'T':
        return 1
    return 0

def win_line(line):
    varxort = 1
    varoort = 1
    for i in range(len(line)):
        if not xort(line[i]):
            varxort = 0
    for i in range(len(line)):
        if not oort(line[i]):
            varoort = 0
    if varxort == 1:
        return 'x'
    if varoort == 1:
        return 'o'
    return 'no'
    
def winner(fourlines):
    for i in range(len(fourlines)):
        temp = win_line(fourlines[i])
        #print 'Line',i, temp
        if temp == 'x':
            return 'X won'
        if temp == 'o':
            return 'O won'
    #print 'vertical'
    for i in range(4): #vertikale
        string = ''
        for j in range(4):
            string += fourlines[j][i]
            #print string
        temp = win_line(string)
        #print i, string, temp
        if temp == 'x':
            return 'X won'
        if temp == 'o':
            return 'O won'
    #print 'diagonal1'
    string = ''
    for i in range(4): #erste diagonale
        string += fourlines[i][i]
        #print string
    temp = win_line(string)
    #print i, string, temp
    if temp == 'x':
        return 'X won'
    if temp == 'o':
        return 'O won'
    string = ''
    for i in range(4): #zweite diagonale
        string += fourlines[i][3-i]
        #print string
    temp = win_line(string)
    #print i, string, temp
    if temp == 'x':
        return 'X won'
    if temp == 'o':
        return 'O won'
    for i in range(4):
        for j in range(4):
            if fourlines[i][j] == '.':
                return 'Game has not completed'
    return 'Draw'

lines = [line.strip() for line in open('google.txt')]
output_file = open("output.txt", 'w')
print lines
for i in range(int(float(lines[0]))):
    case = i+1
    i = i*5
    s = 'Case #' + str(case) + ': ' + winner(lines[i+1:i+5])
    output_file.write(s+'\n')
output_file.close()
