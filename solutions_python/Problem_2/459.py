import sys
# ugly code, but who cares...

def swap(l):
    (st,en) = l.split(" ")
    return en+" "+st

def getFirst():
    if (arev[0]>brev[0]):
        print "brev ",
        print brev
        first = swap(brev[0])
        print first
        brev.remove(brev[0])
        print b
        b.remove(first)
        return (first,0)
    else:
        first = swap(arev[0])
        arev.remove(arev[0])        
        a.remove(first)
        return(first,1)

def getStart(l):
    return int(l.split(" ")[0])

def getEnd(l):
    return int(l.split(" ")[1])

def doCase():
    time = int(lines.pop())
    (at,bt) = lines.pop().split(" ")
    for i in xrange(int(at)):
        a.append(lines.pop().replace(":",""))
    for j in xrange(int(bt)):
        b.append(lines.pop().replace(":",""))
    a.sort()
    b.sort()
    if (len(a) == 0):
        f.write(str(len(b)))
        return
    if (len(b) == 0):
        f.write(str(len(a)))
        return

    for r in a:
        arev.append(swap(r))
    for r in b:
        brev.append(swap(r))
    arev.sort()
    brev.sort()

    print a
    print b
    
    counta = 0
    countb = 0
    while (len(b) > 0) and (len(a) > 0):
        print "-----------------"
        print a
        print b
        (line,who1) = getFirst()
        print line+" "+str(who1)
        if (who1):
            counta += 1
        else:
            countb +=1
       
        have = 1
        who = who1
        while (have):
            if (who):
                i = 0
                while (i < len(b)):
                    if (getEnd(line)+time <= getStart(b[i])):
                        break
                    i += 1             
                if (i < len(b)):
                    line = b[i]
                    who ^= 1
                    brev.remove(swap(b[i]))
                    b.remove(b[i])
                else:
                    have = 0
            else:
                i = 0
                while (i < len(a)):
                    if (getEnd(line)+time <= getStart(a[i])):
                        break
                    i += 1
                if (i < len(a)):
                    line = a[i]
                    who ^= 1
                    arev.remove(swap(a[i]))
                    a.remove(a[i])
                else:
                    have = 0

    countb += len(b)
    counta += len(a)
    f.write(str(counta)+" "+str(countb)+"\n")
        
arev = []
a = []
b = []
brev = []
f = open(sys.argv[1])
lines = f.read().split("\n")
f.close()
f = open('G:\\google\\second\\res.txt','w')
lines.reverse()
times = int(lines.pop())
for i in range(times):
    print "CASE "+str(i+1)
    arev = []
    a = []
    b = []
    brev = []
    f.write("Case #"+str(i+1)+": ")
    doCase()
f.close()

