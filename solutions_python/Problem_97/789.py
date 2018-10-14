import sys, os

reclist = {}
reclist2 = {}
lcount = 0

def makerecycled(a, mi, ma):
    global reclist, lcount, reclist2
    if a in reclist:
        return
    a = str(a)
    myrec = [a]
    b = a
    for i in range(0, len(a) - 1):
        b = b + b[0]
        b = b[1:]
        if (b[0] != "0") and (a != b) and (int(b) > mi) and (int(b) < ma) and (b not in reclist):
            myrec += [b]
    for i in myrec:
        for j in myrec:
            if i != j:
                reclist[i] = True
                reclist[j] = True
                if not (i+j) in  reclist2:
                    lcount += 1
                    reclist2[i+j] = True
                    reclist2[j+i] = True
    
        
if len(sys.argv) > 1:
    f = open(sys.argv[1], 'r')
    fo = open(sys.argv[1] + '.out', 'w')


    cno = int(f.readline())
    print cno

    for c in range(1,cno+1):
        line = f.readline()
        mi, ma = line.split(' ')
        reclist = {}
        reclist2 = {}
        lcount = 0
        print mi + ' ' + ma
        mi = int(mi)
        ma = int(ma)
        for i in range(mi, ma+1):
            makerecycled(i, mi-1, ma+1)
        if c != 1:
            fo.write("\n" + 'Case #'+str(c)+': ' + str(lcount))
        else:
            fo.write('Case #'+str(c)+': ' + str(lcount))
    f.close()
    fo.close()
