f = open('A-small-practice')
t = int(f.readline())
for r in range(1, t+1):
    inpi = f.readline()
    #print(inpi)
    inp = list(map(float, inpi.split()))
    c, fa, x = inp[0], inp[1], inp[2]
    #out = []
    #for i in range(0, 10):
    looking = True
    new = True
    o1 = 0
    o2 = 10000
    i = 0
    while looking:
        #print(looking)
        rate = 2
        time = 0
        for j in range(0, i):
            time+=c/rate
            rate+=fa
        time+=x/rate
        o1 = time
        if o1 > o2 and not new:
            print('Case #{}: {}'.format(r, o2))
            #print(o2, c, fa, x)
            new = False
            looking = False
        new = False
        o2 = o1
        i+=1
        #out.append(time)
    #print(out, c, fa, x)
