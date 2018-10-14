#Small
data = open('C:\CodeJam2012InOut\QualificationRound\ASI.in')
out = open('C:\CodeJam2012InOut\QualificationRound\ASO.out', 'w')
#Large
#data = open('C:\CodeJam2012InOut\QualificationRound\ALI.in')
#out = open('C:\CodeJam2012InOut\QualificationRound\ALO.out', 'w')
lines = data.readlines()
#lines = []
#print lines
i = 1
#words = lines[1].split()

def solve(a, b, c):
    #start
    s = 1
    return s
    
for x in range(int(lines[0])):
    statement = list(lines[x+1])
    print statement
    for y in range(len(statement)):
        if statement[y] == 'a':
            statement[y] = 'y'
        elif statement[y] == 'b':
            statement[y] = 'h'
        elif statement[y] == 'c':
            statement[y] = 'e'
        elif statement[y] == 'd':
            statement[y] = 's'
        elif statement[y] == 'e':
            statement[y] = 'o'
        elif statement[y] == 'f':
            statement[y] = 'c'
        elif statement[y] == 'g':
            statement[y] = 'v'
        elif statement[y] == 'h':
            statement[y] = 'x'
        elif statement[y] == 'i':
            statement[y] = 'd'
        elif statement[y] == 'j':
            statement[y] = 'u'
        elif statement[y] == 'k':
            statement[y] = 'i'
        elif statement[y] == 'l':
            statement[y] = 'g'
        elif statement[y] == 'm':
            statement[y] = 'l'
        elif statement[y] == 'n':
            statement[y] = 'b'
        elif statement[y] == 'o':
            statement[y] = 'k'
        elif statement[y] == 'p':
            statement[y] = 'r'
        elif statement[y] == 'q':
            statement[y] = 'z'
        elif statement[y] == 'r':
            statement[y] = 't'
        elif statement[y] == 's':
            statement[y] = 'n'
        elif statement[y] == 't':
            statement[y] = 'w'
        elif statement[y] == 'u':
            statement[y] = 'j'
        elif statement[y] == 'v':
            statement[y] = 'p'
        elif statement[y] == 'w':
            statement[y] = 'f'
        elif statement[y] == 'x':
            statement[y] = 'm'
        elif statement[y] == 'y':
            statement[y] = 'a'
        elif statement[y] == 'z':
            statement[y] = 'q'
    print statement
    anwser = ''.join(statement)
    print anwser
    #while 578 > 10:
    #    print '5'
    #print words[x]
    #words.append('a')
    #statementl = list(statement)
    #anwser = lines[x+1]
    out.write("Case #%d: %s" %(x+1, anwser))

print 'out'
data.close()
out.close()
