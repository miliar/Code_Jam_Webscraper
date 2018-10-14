def mul(a, b):
    signA, valA = a
    signB, valB = b
    signC, valC = mulDict[valA, valB]
    return (singA*signB*signC, valC)

def reduceString(string):
    sign, val = e
    for char in string:
        signC, val = mulDict[val, char]
        sign *= signC
    return (sign, val)

def wholeProduct(string, X):
    s = reduceString(string)
    signS, valS = s
    sign, val = e
    for x in range(X%4):
        signC, val = mulDict[val, valS]
        sign *= signC * signS
    return sign, val

def ffind(string, desire):
    sign, val = e
    for pos, char in enumerate(string):
        signC, val = mulDict[val, char]
        sign *= signC
        if (sign, val) == desire:
            return pos + 1
    return None

def bfind(string, desire):
    sign, val = e
    for pos, char in enumerate(string[::-1]):
        signC, val = mulDict[char, val]
        sign *= signC
        if (sign, val) == desire:
            return pos + 1
    return None

def solve(caseNo, string, X):
    if wholeProduct(string, X) != ne:
        print('Case #%d: NO' % (caseNo))
        return
    fpos = ffind(string*4, i)
    bpos = bfind(string*4, k)
    if fpos is not None and bpos is not None:
        if bpos + fpos < len(string)*X:
            print('Case #%d: YES' % (caseNo))
            return
    print('Case #%d: No' % (caseNo))

e = (1, '1')
i = (1, 'i')
j = (1, 'j')
k = (1, 'k')
ne = (-1, '1')
ni = (-1, 'i')
nj = (-1, 'j')
nk = (-1, 'k')
mulDict = {('1', '1'):e, ('1', 'i'):i,  ('1', 'j'):j,  ('1', 'k'):k,
           ('i', '1'):i, ('i', 'i'):ne, ('i', 'j'):k,  ('i', 'k'):nj,
           ('j', '1'):j, ('j', 'i'):nk, ('j', 'j'):ne, ('j', 'k'):i,
           ('k', '1'):k, ('k', 'i'):j,  ('k', 'j'):ni, ('k', 'k'):ne}

fin = open('C-large.in')

caseNum = int(fin.readline())

for caseNo in range(caseNum):
    tokens = fin.readline().strip().split()
    L = int(tokens[0])
    X = int(tokens[1])
    string = fin.readline().strip()
    solve(caseNo+1, string, X)

fin.close()
