def quatMult(a, b):
    neg = False
    neg ^= (a[0] == '-')
    neg ^= (b[0] == '-')
    a = a.replace('-', '')
    b = b.replace('-', '')
    res = ''
    if(a == '1'):
        res = b
    if(b == '1'):
        res = a
    if(a == 'i'):
        if(b == 'i'):
            res = '1'
            neg ^= True
        if(b == 'j'):
            res = 'k'
        if(b == 'k'):
            res = 'j'
            neg ^= True
    if(a == 'j'):
        if(b == 'i'):
            res = 'k'
            neg ^= True
        if(b == 'j'):
            res = '1'
            neg ^= True
        if(b == 'k'):
            res = 'i'
    if(a == 'k'):
        if(b == 'i'):
            res = 'j'
        if(b == 'j'):
            res = 'i'
            neg ^= True
        if(b == 'k'):
            res = '1'
            neg ^= True
    if neg:
        res = '-' + res
    return res
        

def cutOffChar(string, char):
    temp = '1'
    resindex = 0
    for i in range(len(string)):
        temp = quatMult(temp, string[i])
        if temp == char:
            return string[i+1:]
    return "Impossible"

def reduceComplete(string):
    temp = '1'
    for i in range(len(string)):
        temp = quatMult(temp, string[i])
    return temp

def reduceDijkstra(string):
    string = cutOffChar(string, 'i')
    if string == "Impossible":
        return False
    string = cutOffChar(string, 'j')
    if string == "Impossible":
        return False
    string = cutOffChar(string, 'k')
    if string == "Impossible":
        return False
    string = reduceComplete(string)
    return string == '1'


fin = open('C-small-attempt0.in', 'r')
fout = open('C-small-attempt0.out', 'w')
T = int(fin.readline())
for t in range(T):
    args = fin.readline().replace("\n", "").split(" ")
    L = int(args[0])
    X = int(args[1])
    string = fin.readline().strip()*X
    if reduceDijkstra(string):
        print "Yes"
        fout.write("Case #" + str(t+1) + ": YES\n")
    else:
        print "No"
        fout.write("Case #" + str(t+1) + ": NO\n")
fin.close()
fout.close()
            
