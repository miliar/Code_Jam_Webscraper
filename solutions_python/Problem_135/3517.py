
t = int(input())
for i in xrange(t):
    r1 = int(input())
    for j in xrange(4):
        strIn = raw_input()
        if r1 == j+1 :
            r1set = set([int(e) for e in strIn.split()])
            
    r2 = int(input())
    for j in xrange(4):
        strIn = raw_input()
        if r2 == j+1 :
            r2set = set([int(e) for e in strIn.split()])
    inter =r1set.intersection(r2set)
    count = len(inter)

    if count==0:
        print 'Case #'+str(i+1)+': Volunteer cheated!'
    elif count == 1:
         print 'Case #'+str(i+1)+': '+str(inter.pop())
    else:
         print 'Case #'+str(i+1)+': Bad magician!'
        
