import numpy as np

def process(s):
    cs = ('X','O')

    for c in cs:
        ts = s.replace('T',c)
        a = np.array([[x==c for x in ss] for ss in ts.split('\n') 
                                           if ss.strip()])

        rows, cols = a.shape

        for i in range(rows):
            if np.all(a[i,:]):
                return '%s won'%c
        for j in range(cols):
            if np.all(a[:,j]):
                return '%s won'%c

        if np.all(a.diagonal()):
            return '%s won'%c
        if np.all(np.fliplr(a).diagonal()):
            return '%s won'%c
   
    a = np.array([[x=='.' for x in ss] for ss in s.split('\n')
                                         if ss.strip()])
    if a.any():
        return 'Game has not completed'
    return 'Draw'


def run(inpath, outpath):
    fin = open(inpath, 'rU')
    fout = open(outpath, 'w')

    s = ''
    case = 1
    for i, line in enumerate(fin):
        if not i:
            continue
        
        if not line.strip():
            res = process(s)
            cstr = 'Case #%d: %s\n'%(case, res)

            print cstr[:-1]
            fout.write(cstr)

            case += 1
            s = ''

        s += line

    fin.close()
    fout.close()
