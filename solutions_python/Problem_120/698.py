


def inkRequired(outterradi):
    return (outterradi**2)-((outterradi-1)**2)

def startDrawing(radi,ink):
    inwhite = radi
    black = radi+1
    while inkRequired(black)<=ink:
        yield black
        ink -= inkRequired(black)
        black+=2

test_cases = long(raw_input())
for i in range(test_cases):
    line = raw_input()
    inp = line.split()
    ink = long(inp[1])
    radi = long(inp[0])
    count = 0
    for newradi in startDrawing(radi,ink):
        count+=1
    print "Case #"+str(i+1)+": "+str(count)
