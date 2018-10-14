


f = open('quals_A.in')
fout = open('quals_A.out','w')

n_input = int(f.readline())

# print n_input + 1

def check(line):
    line = list(line)

    #print "checking " + str(line)
    while 'T' in line:
        line.remove('T')
    #print "checking " + str(line)
    if '.' in line or False in [line[0]==a for a in line]:
        return None
    else:
        #print "Here's something! It's " + line[0]
        return line[0]

out = ""

for i_input in range(n_input):
    rows = [f.readline().rstrip('\n') for j in range(4)]

    cols = [[rows[i][j] for i in range(4)] for j in range(4)]
    diags = [ [rows[i][i] for i in range(4)], [rows[i][3-i] for i in range(4)] ]

    lines = rows + cols + diags
    checks = [check(line) for line in lines]

    out += "Case #" + str(i_input+1) + ": "
    
    if 'X' in checks:
        out += "X won\n"
    elif 'O' in checks:
        out += "O won\n"
    elif True in ['.' in row for row in rows]:
        out += "Game has not completed\n"
    else:
        out += "Draw\n"

    
    
    f.readline()


f.close()
fout.write(out)
fout.close()
