#http://docs.python.org/release/2.3.5/whatsnew/section-slices.html


def palindrone(a):
    a = str(a)
    b = a[::-1]
    return b == a

def findroot(a):
    return int(a**(0.5))    

def checkFit(inCase):
    #Check line by line
    mCase = inCase
    for i in mCase:
        if 'XXXT' in i:
            return 'X won'
        if 'XXXX' in i:
            return 'X won'
    for i in mCase:
        if 'OOOT' in i:
            return 'O won'
        if 'OOOO' in i:
            return 'O won'
    #Check column by column
    for i in range(4):
        if 'XXXX' in "".join(list(zip(*inCase)[i])):
            return 'X won'
        if 'XXXT' in "".join(list(zip(*inCase)[i])):
            return 'X won'
    for i in range(4):
        if 'OOOT' in "".join(list(zip(*inCase)[i])):
            return 'O won'
        if 'OOOO' in "".join(list(zip(*inCase)[i])):
            return 'O won'

    #Check diagonal by diagonl
    if 'OOOO' in "".join([r[-i-1] for i, r in enumerate(inCase)]):
        return 'O won'

    if 'OOOT' in "".join([r[-i-1] for i, r in enumerate(inCase)]):
        return 'O won'

    if 'TOOO' in "".join([r[-i-1] for i, r in enumerate(inCase)]):
        return 'O won'

    #Search leading diagonal
    if 'OOOO' in "".join([r[i] for i, r in enumerate(inCase)]):
        return 'O won'

    if 'OOOT' in "".join([r[i] for i, r in enumerate(inCase)]):
        return 'O won'

    if 'TOOO' in "".join([r[i] for i, r in enumerate(inCase)]):
        return 'O won'


    if 'XXXX' in "".join([r[-i-1] for i, r in enumerate(inCase)]):
        return 'X won'

    if 'XXXT' in "".join([r[-i-1] for i, r in enumerate(inCase)]):
        return 'X won'
    if 'TXXX' in "".join([r[-i-1] for i, r in enumerate(inCase)]):
        return 'X won'

    #Search leading diagonal
    if 'XXXX' in "".join([r[i] for i, r in enumerate(inCase)]):
        return 'X won'

    if 'XXXT' in "".join([r[i] for i, r in enumerate(inCase)]):
        return 'X won'

    if 'TXXX' in "".join([r[i] for i, r in enumerate(inCase)]):
        return 'X won'
    #Collapse the entire set and see if "." is absent invoke draw else invoke not completed


    if '.' in ''.join(inCase):
        return 'Game has not completed'

    return 'Draw'



f = open('A-small-attempt3.in', 'r')
g = open('A-small-attempt3.out','w')

T = int(f.readline()) #number of test cases
for j in range(T):
    Case=[]
    for i in range(4):
        Case.append((f.readline()).strip())
    f.readline() #For the empty line
    print Case
    print "Case #"+ str(j+1) + ": " + checkFit(Case)+"\n"
    g.write("Case #"+ str(j+1) + ": " + checkFit(Case)+"\n")

g.close()
f.close()
        

