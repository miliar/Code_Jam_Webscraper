import os

h = open('B-large.in', 'r')
out = open('output.txt','w')

l = h.readline()
n = int(l); #no. of cases

for x in range(n):
    l = h.readline()
    l = l.split(' ')
    combines = {}
    opposites = []

    lIdx = 0 
    nc = int(l[lIdx])
    for i in range(nc):
        lIdx = lIdx + 1
        ce = l[lIdx]
        combines[''.join(sorted(ce[:2]))] = ce[2::]

    lIdx = lIdx + 1
    no = int(l[lIdx])
    for i in range(no):
        lIdx = lIdx + 1
        oe = l[lIdx]
        opposites.append(''.join(sorted(oe[:2])))

    lIdx = lIdx + 1
    nElems = int(l[lIdx])

    ans = []
    if (nElems > 0):
        lIdx = lIdx + 1
        elems = l[lIdx]
        ans.append(elems[0])

        for i in range(1, nElems):
            e = elems[i]
            ans.append(e)

            while(len(ans) > 1):
                temp = ans[-2] + ans[-1]
                possibleCombine = ''.join(sorted(temp))
                if(possibleCombine in combines):
                    del(ans[-1])
                    ans[-1] = combines[possibleCombine]
                else:
                    break

            nans = len(ans)
            if(nans > 1):
                for j in range(nans - 1):
                    temp = ans[j] + ans[-1]
                    possibleOpposite = ''.join(sorted(temp))
                    if(possibleOpposite in opposites):
                        del ans[:]
                        break

    outstr = 'Case #' + str(x+1) + ': ' + str(ans).replace('\'','')
    out.write(outstr)
    if(n-x != 1):
        out.write('\n')
    
h.close()
out.close()
