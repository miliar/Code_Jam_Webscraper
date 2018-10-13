import math

f = open('D-small-attempt1.in', 'r')
g = open('output', 'w')

data = [line for line in f]
T = data.pop(0)

for case, d in enumerate(data):
    X, R, C = [int(i) for i in d.split()]
    winner = ""
    P = R*C
    if X > 6:
        winner = "RICHARD"
    elif P % X:
        winner = "RICHARD"
    elif (R < math.floor(X/2.)+1 or C < math.floor(X/2.)+1) and X > 2:
        winner = "RICHARD"
    else:
        winner = "GABRIEL"
            
        
    
    print 'Case #%d: %s' %(case + 1, winner)
    g.write('Case #%d: %s\n' %(case + 1, winner))

f.close()
g.close()
