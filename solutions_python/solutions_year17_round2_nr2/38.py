import sys
import numpy as np
from collections import Counter

def getWords():
    return sys.stdin.readline().strip().split()

def getInts():
    return np.array([int(i) for i in getWords()], dtype=np.int64)

def getInt():
	i = getInts()
	assert len(i)==1
	return i[0]

allowed = {
'R':set('GBY'),
'B':set('ORY'),
'Y':set('VBR'),
'G':set('R'),
'O':set('B'),
'V':set('Y'),
}

#sys.stdin = open('B.in')

T = getInt()
for caseNo in xrange(1,T+1):
    N, R, O, Y, G, B, V = getInts()
    assert R + O + Y + G + B + V == N
    col = np.asarray([[R,B,Y],[G,O,V]])
    letter = ("RBY","GOV")
    
    basecol = col[0] - col[1]
    if basecol.min() < 0 or 2*basecol.max() > basecol.sum():
        res = "IMPOSSIBLE"
    # equal, nonzero count of e.g. R and G - only good if no other letters exist
    elif ( (basecol==0) & (col[1]>0) ).any():
        if (col[0]>0).sum() == 1:
            i = np.argmax(col[0])
            res = (letter[0][i] + letter[1][i]) * (N//2)
        else:
            res = "IMPOSSIBLE"
    else:
        res = ""
        secondaryColourPushed = np.zeros(3, dtype=bool)
        iterNum = basecol.sum()
        # tie-breaking: hack to make sure the first primary colour isn't repeated at the end
        basecol = np.asarray(basecol, dtype=float)
        basecol[np.argmax(basecol)] += 0.5
        # currently used colour
        c = -1
        for i in xrange(iterNum):
            c = np.argmax( basecol * (np.arange(3)!=c) )
            basecol[c] -= 1
            if not secondaryColourPushed[c]:
                res += (letter[0][c] + letter[1][c]) * col[1][c]
                secondaryColourPushed[c] = True
            res += letter[0][c]


    #print caseNo
    print "Case #%d: %s"%(caseNo, res)
    #debug residue
    if res=='IMPOSSIBLE':
        pass
        #print col
    else:
        ct = Counter(res)
        #print col
        #print ct
        for i in range(2):
            for c in range(3):
                assert col[i][c] == ct[letter[i][c]]
        for i in xrange(N-1):
            assert res[i] in allowed[res[i+1]]
        assert res[N-1] in allowed[res[0]]

