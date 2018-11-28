f = open('d.in')
out = open('d.out', 'w+')
t = int(f.readline())
def res(blocks, choice):
    if choice > blocks[len(blocks)-1]:
        return blocks[0]
    else:
        i = 0
        while blocks[i] < choice:
            i+=1
        return blocks[i]
for tc in range(t):
    f.readline()
    nao = sorted([float(a) for a in f.readline().split()])
    ken = sorted([float(a) for a in f.readline().split()])
    fnao = nao[:]
    fken = ken[:]
    fscore = 0
    score = 0
    while len(nao) > 0:
        fn = fnao.pop(len(fnao)-1)
        fk = fken.pop(fken.index(res(fken, fn)))
        if fn > fk:
            fscore += 1
        if min(nao)<min(ken):
            nao.pop(0)
            ken.pop(len(ken)-1)
        else:
            nao.pop(0)
            ken.pop(0)
            score += 1
    out.write('Case #{0}: {1} {2}\n'.format(tc+1, score, fscore))
        
        
        
        
