from decimal import *
getcontext().prec = 6
#Small
data = open('C:\CodeJam2012InOut\Round1A\ASI.in')
out = open('C:\CodeJam2012InOut\Round1A\ASO.out', 'w')
#Large
#data = open('C:\CodeJam2012InOut\Round1A\ALI.in')
#out = open('C:\CodeJam2012InOut\Round1A\ALO.out', 'w')
lines = data.readlines()
#lines = []
#print lines
i = 1
#words = lines[1].split()

def solve(a, b, c):
    return s
    
for x in range(int(lines[0])):
    x = x*2
    letters = lines[x+1].split()
    print letters
    probability = lines[x+2].split()
    print probability
    currentmin = int(letters[1]) + 2
    newmin = 1000000000000000
    prob = 1
    for y in range(int(letters[0])):
        prob = prob * float(probability[y])
    newmin = prob * ((int(letters[1]) - int(letters[0])) + 1) + (1-prob) * ((int(letters[1]) - int(letters[0]) + int(letters[1])) +2)
    if newmin <= currentmin:
        currentmin = newmin
    prob = 1
    for z in range(int(letters[0])):
        print 'ok'
        for a in range(int(letters[0])):
            if (a - z - 1) >= 0:
                try:
                    #print probability[a - z - 1]
                    prob = prob * float(probability[a - z - 1])
                except:
                    prob = prob
        newmin = z + 1 + z +1 + int(letters[1]) - int(letters[0]) + 1 + (1-prob) * ((int(letters[1]) + 1))
        print newmin
        if newmin <= currentmin :
            currentmin = newmin
        prob = 1 

        
    #while 578 > 10:
    #    print '5'
    #print words[x]
    #words.append('a')
    #statementl = list(statement)
    #anwser = lines[x+1]
    anwser = Decimal(currentmin)/Decimal(1)
    
    out.write("Case #%d: %s\n" %(x+1, anwser))

print 'out'
data.close()
out.close()
