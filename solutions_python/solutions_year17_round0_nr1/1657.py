def opp(c):
    if c=='+':
        return '-'
    elif c=='-':
        return '+'
    else:
        assert False

fi=open('ex1-large.in')
fo=open('ex1-large.out','w')
nCases=int(fi.readline())
for case in range(1,nCases+1):
    pancakes,flipSize=fi.readline().split()
    pancakes=list(pancakes)
    flipSize=int(flipSize)
    flips=0
    for i in range(len(pancakes)-flipSize+1):
        if pancakes[i]=='-':
            flips+=1
            for j in range(i,i+flipSize):
                pancakes[j]=opp(pancakes[j])
    if '-' not in pancakes:
        fo.write('Case #%s: %s\n' % (case,flips))
    else:
        fo.write('Case #%s: IMPOSSIBLE\n' % case)
fi.close()
fo.close()
