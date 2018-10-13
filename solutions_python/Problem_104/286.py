import itertools
def probC():
    f=open('input.txt','r')
    new=open('answer.txt','w')
    for tc in xrange(1, int(f.readline())+1):
        newmap={}
        array=[int(w) for w in f.readline().split()]
        number=array[0]
        scores=array[1:]
        found=False
        for e in range(1,20):
            if found:
                break
            combos=itertools.combinations(scores,e)
            for combo in combos:
                summe=sum(combo)
                if summe in newmap:
                    new.write('Case #%d:\n' % (tc))
                    new.write(newmap[summe]+"\n")
                    new.write(' '.join(map(str,combo))+"\n")
                    found=True
                    break
                newmap[summe]=' '.join(map(str,combo))
        if not found:
            new.write('Case #%d:\n%s' % (tc,'Impossible')+"\n")
