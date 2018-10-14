inputname = 'C-small-attempt1.in'
outputname = 'output.out'
f = open(inputname)
fw = open(outputname, 'w')

T = int(f.readline().strip())

def multi(x,y): 
    
    if x==1:
        return 1, y
    if y==1:
        return 1, x
    if x==y:
        return -1,1

    if x=='i':
        return (1,'k') if y == 'j' else (-1,'j')
    if x=='j':
         return (1,'i') if y == 'k' else (-1,'k')
    if x=='k':
        return (1,'j') if y == 'i' else (-1,'i')


for t in range(T):
    L, X = (int(x) for x in f.readline().strip().split())

    d=f.readline().strip()

    residue= X % 4

    if residue == 0 or L==1 or residue*L < 3:
        fw.write('Case #%d: NO\n' % (t + 1))
        continue


    # Determine if the list converges to -1
    c=d[0]
    sign =1
    for i in range(1,L):
        s, c=multi(c, d[i])
        sign *= s

    sign =1 if residue%2==0 else sign

    temp=c
    for i in range(1,residue):
        s,c=multi(c,temp)
        sign *= s

    if not sign == -1 or not c==1:
        fw.write('Case #%d: NO\n' % (t + 1))
        continue

    # If converges to -1
    toBeFound='ijk'
    sign =1
    toBeFoundInd=0
    start=1

    for j in range(X):
        for i in range(L):
            if start:
                c=d[i]
                start=0
            else:
                s, c=multi(c, d[i])
                sign *= s

            if c == toBeFound[toBeFoundInd]:
                toBeFoundInd +=1
                start=1
                if toBeFoundInd==3:
                    break

        if toBeFoundInd ==3:
            break

    if toBeFoundInd==3:
        fw.write('Case #%d: YES\n' % (t + 1))
    else:
        fw.write('Case #%d: NO\n' % (t + 1))

f.close()
fw.close()
