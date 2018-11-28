f = file('input.in','r')
inpstrs = f.readlines()
f.close()
def subsets(mySet):
    return reduce(lambda z, x: z + [y + [x] for y in z], mySet, [[]])

t = int(inpstrs[0])
for i in range(1,len(inpstrs)) :
    strs = inpstrs[i].split(' ')
    n = int(strs[0])
    inplst = []
    for j in range(0,n) :
        inplst.append(strs[j+1])
    subsets = reduce(lambda z, x: z + [y + [x] for y in z], inplst, [[]])
    summap = {}
    for k in subsets :
        sset = 0
        for l in k :
            sset += int(l)
        if sset in summap :
            print "Case #"+str(i)+":"
            for m in k :
                print m,
            print
            for x in summap[sset] :
                print x,
            print            
            break
        else :
            summap[sset] = k
