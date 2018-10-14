def readint(input):
    return int(input.readline().strip('\n'))

def readstr(input):
    return input.readline().strip('\n')


def readintline(intput):
    return [int(i) for i in input.readline().strip('\n').split(' ')]

def readstrline(intput):
    return [i for i in input.readline().strip('\n').split(' ')]
    
    
mult = {
    '11':'1','1i':'i','1j':'j','1k':'k',
    '-1-1':'1','-1-i':'i','-1-j':'j','-1-k':'k',
    '1-1':'-1','1-i':'-i','1-j':'-j','1-k':'-k',
    '-11':'-1','-1i':'-i','-1j':'-j','-1k':'-k',
    
    'i1':'i','ii':'-1','ij':'k','ik':'-j',
    '-i-1':'i','-i-i':'-1','-i-j':'k','-i-k':'-j',
    '-i1':'-i','-ii':'1','-ij':'-k','-ik':'j',
    'i-1':'-i','i-i':'1','i-j':'-k','i-k':'j',

    'j1':'j','ji':'-k','jj':'-1','jk':'i',
    '-j-1':'j','-j-i':'-k','-j-j':'-1','-j-k':'i',
    'j-1':'-j','j-i':'k','j-j':'1','j-k':'-i',
    '-j1':'-j','-ji':'k','-jj':'1','-jk':'-i',

    'k1':'k','ki':'j','kj':'-i','kk':'-1',
    '-k-1':'k','-k-i':'j','-k-j':'-i','-k-k':'-1',
    'k-1':'-k','k-i':'-j','k-j':'i','k-k':'1',
    '-k1':'-k','-ki':'-j','-kj':'i','-kk':'1'
}

   
def solve(L,X,word):
    total = L * X
    
    #check mult of word
    mword = '1'
    for i in xrange(total):
        mword = mult[mword+word[i % L]]
    
    if mword != '-1':
        return 'NO'
    
    cI = 0
    mI = '1'
    #compute each result
    while cI < total:
        mI = mult[mI+word[cI % L]]
        if mI == 'i':
            #try to avance with j now
            cJ = cI + 1
            mJ = '1'
            #print 'advance to J at', cJ
            while cJ < total:
                mJ = mult[mJ+word[cJ  % L]]
                if mJ == 'j':
                    #check if rest produces k
                    cK = cJ + 1
                    mK = '1'
                    #print 'advance to K at', cK
                    while cK < total:
                        mK = mult[mK+word[cK % L]]
                        cK += 1
                    if mK == 'k':
                        return 'YES'
                cJ += 1
        cI += 1
    
    return 'NO'

with open('C-small-attempt2.in','r') as input:
    with open('C-small-attempt2.out','w') as output:
        cases = readint(input)
        for case in xrange(1,cases+1):
            values = readintline(input)
            #print values
            L = values[0]
            X = values[1]
            word = readstr(input)
            #print L, X, word
            result = solve(L,X,word)
            output.write('Case #%s: %s\n' % (str(case),str(result)))

print 'Done'