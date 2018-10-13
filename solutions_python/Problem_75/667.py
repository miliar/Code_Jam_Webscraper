def getdata():
    inp = raw_input().split()
    C = int(inp[0])
    inp = inp[1:]
    transformations = inp[0:C]
    inp = inp[C:]
    D = int(inp[0])
    inp = inp[1:]
    opposed = inp[0:D]
    inp = inp[D:]
    N = int(inp[0])
    seq = inp[1:][0]
    return transformations , opposed, seq

def formatList(x):
    return '[' + ', '.join(x) + ']'

t = int(raw_input())

for i in range(t):
    combine, opposed, seq = getdata()
    
    transdict= {}
    for transformation in combine:
        transdict[transformation[:2]] = transformation[-1]
    
    elementList = []
    for char in seq:
        elementList.append(char)
        replaced = False
        if len(elementList) == 1:
            continue
        else:
            combination = elementList[-1] + elementList[-2]
            x = transdict.keys()
            if combination in x :
                elementList = elementList[:-2]
                elementList.append(transdict[combination])
                replaced = True
            elif combination[::-1] in x:
                elementList = elementList[:-2]
                elementList.append(transdict[combination[::-1]])
                replaced = True
            
            if not replaced:
                for combo in opposed:
                    if combo[0] in elementList and combo[1] in elementList:
                        elementList = []

    print "Case #%d:" %( i+1), formatList(elementList)
