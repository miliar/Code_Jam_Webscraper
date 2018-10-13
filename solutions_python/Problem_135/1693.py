f = open('A-small-practice')
t = int(f.readline())
for r in range(1, t+1):
    ln1 = int(f.readline())
    for i in range(1, 5):
        if i == ln1:
            inpi = f.readline()
            line1 = list(map(int, inpi.split()))
        else:
            dstn = f.readline()
    ln2 = int(f.readline())
    for i in range(1, 5):
        if i == ln2:
            inpi = f.readline()
            line2 = list(map(int, inpi.split()))
        else:
            dstn = f.readline()
    common = list(set(line1) & set(line2))
    if len(common) == 1:
        print('Case #{}: {}'.format(r, common[0]))
        #print(common[0])
    elif len(common) == 0:
        print('Case #{}: Volunteer cheated!'.format(r))
        #print('Volunteer cheated!')
    else:
        print('Case #{}: Bad magician!'.format(r))
        #print('Bad magician!')
        


##    inpi = f.readline()
##    #print(inpi)
##    inp = list(map(float, inpi.split()))
##    c, fa, x = inp[0], inp[1], inp[2]
##    #out = []
##    #for i in range(0, 10):
##    looking = True
##    new = True
##    o1 = 0
##    o2 = 10000
##    i = 0
##    while looking:
##        #print(looking)
##        rate = 2
##        time = 0
##        for j in range(0, i):
##            time+=c/rate
##            rate+=fa
##        time+=x/rate
##        o1 = time
##        if o1 >= o2 and not new:
##            print('Case #{}: {}'.format(r, o2))
##            #print(o2, c, fa, x)
##            new = False
##            looking = False
##        new = False
##        o2 = o1
##        print(o2)
##        i+=1
##        #out.append(time)
##    #print(out, c, fa, x)
##
