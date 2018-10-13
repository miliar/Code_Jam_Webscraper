# Alien Language

import re

infile=open('A-large.in')

if __name__ == '__main__':
    L,D,N=[int(x) for x in infile.readline().split()]
    words=''
    for i in range(D):
        words+=infile.readline()
    for i in range(N):
        case=infile.readline().strip()
        case=case.replace('(','[')
        case=case.replace(')',']{1}')
        cases=len(re.findall(case,words))
        print 'Case #%s: %s' % (i+1,cases)
