# ertug (Ertug Karamatli)

import sys
import re

f = file(sys.argv[1])

ln = 0

    
num_rep={10:'a',
     11:'b',
     12:'c',
     13:'d',
     14:'e',
     15:'f',
     16:'g',
     17:'h',
     18:'i',
     19:'j',
     20:'k',
     21:'l',
     22:'m',
     23:'n',
     24:'o',
     25:'p',
     26:'q',
     27:'r',
     28:'s',
     29:'t',
     30:'u',
     31:'v',
     32:'w',
     33:'x',
     34:'y',
     35:'z'
}
nd={}
for k,v in num_rep.iteritems():
    nd.update({v:k})

case = 1
for line in f:
    if line == '': continue
    if ln != 0:
        X = list(line)[:-1]

        i=0
        cd = 1
        toRep = X[i]
        for j in xrange(len(X)):
            if X[j] == toRep: X[j] = cd

        cd = 0
        for i in xrange(1,len(X)):
            toRep = X[i]
            if type(toRep) == str:
                for j in xrange(len(X)):
                    if type(X[j]) == str:
                        if X[j] == toRep: X[j] = cd
                cd += 1
                if cd == 1: cd = 2

        pos=0
        base = max(X)+1
        minn = 0
        for d in X:
            val = pow(base,len(X)-pos-1)
            minn+=val*d

            pos+=1

        print 'Case #%s: %s' % (case, minn)

        case += 1
        sys.stdout.flush()

    ln += 1

