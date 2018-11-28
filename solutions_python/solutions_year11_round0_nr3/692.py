f = open("C-large.in")
data = f.readlines()
f.close()
data = map(str.strip, data)

resout = []
for testcase in data[2::2]:
    found = False
    ar = testcase.split(' ')
    ar = map(int, ar)
    ar.sort()
    print "Input: ", ar
    for i in range(1, len(ar)):
        print i
        paul = ar[0]
        for j in range(1, i):
            paul = paul ^ ar[j]
        print "Paul:", paul
        
        sean = ar[i]
        for j in range(i+1, len(ar)):
            sean = sean ^ ar[j]
        print "Sean:", sean
        
        if paul == sean:
            found = True
            break
            
    if found:
        print "Breakpoint:", i
        print "Sean's bag value:", sum(ar[i:])
        resout.append(sum(ar[i:]))
    else:
        resout.append("NO")


f = open("C-large.out", 'w')
for i, r in enumerate(resout):
    f.write("Case #%d: %s\n" % (i+1, r))
f.close()
        