def tokenize(word):
    state='CHAR'
    repo=[]
    for c in word:
        if c=='(':
            state='COLLECTING'
        elif c==')':
            yield repo
            state='CHAR'
            repo=[]
        else:
            if state=='CHAR':
                yield [c]
            elif state=='COLLECTING':
                repo.append(c)
            else:
                raise ValueError('should not be here')

def posible_interpretation(dictionary, word):
    cnt=0
    tokens=list(tokenize(word))
    for dw in dictionary:
        for i,dc in enumerate(dw):
            #print 'dc: %s, token: %s' % (dc, tokens[i])
            if not dc in tokens[i]:
                break
        else:
            cnt+=1
    return cnt

import sys
def read_n():
    return [int(n) for n in sys.stdin.readline().split()]

def read_nlines(n):
    for i in range(n):
        yield sys.stdin.readline().strip()

L,D,N=read_n()
dictionary=list(read_nlines(D))
cases=list(read_nlines(N))

for i, testcase in enumerate(cases):
    print 'Case #%d: %d' % (i+1,
        posible_interpretation(dictionary, testcase))

