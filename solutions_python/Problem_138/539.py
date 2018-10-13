title = 'D'
scale = 'large'

fpout = open(title + '-' + scale + '.out', 'w')
def presult(casenum, s):
    fpout.write('Case #' + str(casenum) + ': ' + s + '\n')



f = open(title + '-' + scale + '.in', 'r')


num_case = int(f.readline().rstrip())

for casen in range(1, num_case+1):
    waste = f.readline()
    naomis = [ float(x) for x in f.readline().strip().split(' ') ]
    kens = [ float(x) for x in f.readline().strip().split(' ') ]
    
    anaomis = sorted(naomis)
    dnaomis = sorted(naomis, reverse=True)
    akens = sorted(kens)
    dkens = sorted(kens, reverse=True)

    losetuple = 0
    store = 0
    
    for i in range(0, 2*len(naomis)):
        nnext = anaomis[0] if len(anaomis) != 0 else 100
        knext = akens[0] if len(akens) != 0 else 100
        if nnext < knext:
            anaomis.pop(0)
            if store > 0:
                store -= 1
            else:
                losetuple += 1
        else:
            akens.pop(0)
            store += 1
    y = len(naomis) - losetuple

    wintuple = 0
    store = 0

    for j in range(0, 2*len(naomis)):
        nnext = dnaomis[0] if len(dnaomis) != 0 else -1
        knext = dkens[0] if len(dkens) != 0 else -1
        if nnext > knext:
            dnaomis.pop(0)
            if store > 0:
                store -= 1
            else:
                wintuple += 1
        else:
            dkens.pop(0)
            store += 1
    z = wintuple

    presult(casen, str(y) + ' ' + str(z))
        
            


