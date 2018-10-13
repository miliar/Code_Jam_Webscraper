def tokens(_str):
    orMode = False
    r = []
    tok = []
    for s in _str:
        if s=='(':
            orMode = True
        elif s==')':
            r.append(tok[:])
            tok=[]
            orMode = False
        else:
            tok.append(s)
            if not orMode:
                r.append(tok[:])
                tok = []
    return r

def match(ptok, word):
    if len(ptok)!=len(word):
        return False
    return all([w in ptok[i] for i, w in enumerate(word)])

def solve(pattern, dic):
    pTok = tokens(pattern)
    count = 0
    for word in dic:
        if match(pTok, word):
            count = count+1
    return count

fin = open('A-large.in', 'r')
fout = open('out.txt', 'w')
F = [int(s) for s in fin.readline().split()]
dic = []
for i in range(F[1]):
    dic.append(fin.readline())
for i in range(1, F[2]+1):
    s = solve(fin.readline(), dic)
    print('Case #%d: %d'%(i, s))
    fout.write('Case #%d: %d\n'%(i, s))
fout.close()
fin.close()
                
