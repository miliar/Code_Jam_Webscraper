f = open('A-large.in')
outf = open('result.txt','w')

def makeDTree(treestr):
    dtree = []
    treestr = treestr[1:].lstrip()
    lsubtree = []
    rsubtree = []
    
    token = ''

    spidx = 0
    rpidx = treestr.find(')')
    weight = 0.0
    feat = ''

    while treestr[0] != ')':

        spidx = treestr.find(' ')

        if treestr[0].isdigit():
            if spidx < rpidx:
                token = treestr[:spidx]
                dtree.append(float(token))
                treestr = treestr[spidx+1:]
            else:
                token = treestr[:rpidx]
                dtree.append(float(token))
                treestr = treestr[rpidx:]

        elif treestr[0].islower():
            feat = treestr[:spidx]
            treestr = treestr[spidx+1:]

        elif treestr[0] == '(':
            lsubtree, treestr = makeDTree(treestr)
            rsubtree, treestr = makeDTree(treestr)

    treestr = treestr[1:].lstrip()

    dtree.append(feat)
    dtree.append(lsubtree)
    dtree.append(rsubtree)

    return dtree, treestr

def getAnimal(anistr):
    anistr = anistr.split()
    name = anistr[0]
    anistr = anistr[2:]
    feats = []

    for x in anistr:
        feats.append(x)

    return (name, feats)

def outPosb(dtree, ani):
    pos = 10000000

    while 1:
        pos = pos * dtree[0]

        if dtree[1] != '':
            try:
                ani[1].index(dtree[1])
                dtree = dtree[2]
            except ValueError:
                dtree = dtree[3]
        else:
            break

    res = str(int(pos))
    l = len(res)

    if res == '10000000':
        res = '1.0000000'
    else:
        if l > 7:
            res = res[:7]
        elif l < 7:
            res = '0'*(7-l)+res

        res = '0.'+res
            
    outf.write(res+'\n')
    
def main():
    nCase = int(f.readline())

    for x in range(nCase):
        outf.write('Case #'+str(int(x+1))+':\n')
        nLine = int(f.readline())
        line = ''
        for y in range(nLine):
            line = line + f.readline().lstrip().rstrip()+' '
        dtree, line = makeDTree(line)

        nLine = int(f.readline())
        for y in range(nLine):
            outPosb(dtree, getAnimal(f.readline()))

if __name__ == '__main__':
    main()
    f.close()
    outf.close()
