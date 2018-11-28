#Small
#data = open('C:\CodeJam2012InOut\QualificationRound\BSI.in')
#out = open('C:\CodeJam2012InOut\QualificationRound\BSO.out', 'w')
#Large
data = open('C:\CodeJam2012InOut\QualificationRound\BLI.in')
out = open('C:\CodeJam2012InOut\QualificationRound\BLO.out', 'w')
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
    current = lines[x+1].split()
    #print current
    anwser = 0
    supprise = int(current[1])
    score = int(current[2])
    #print x+1
    #print 'UYRHAERHEHYS'
    for y in range(int(current[0])):
        #print int(current[y+3])
        #print (score*3-2)
        if int(current[y+3]) >= (score*3-2):
            anwser = anwser + 1
        elif supprise > 0 and int(current[y+3]) >= (score*3-4) and int(current[y+3]) != 0:
            anwser = anwser + 1
            supprise = supprise - 1
    #while 578 > 10:
    #    print '5'
    #print words[x]
    #words.append('a')
    #statementl = list(statement)
    #anwser = lines[x+1]
    out.write("Case #%d: %s\n" %(x+1, anwser))

print 'out'
data.close()
out.close()
