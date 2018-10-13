f = open('A-small-attempt0.in', 'r')

T = int(f.readline().strip())
row=4

r=map(int,[0 for col in range(T)])
v=[0 for col in range(T)]

for t in xrange(T):

    A = int(f.readline().strip())

    for a in xrange(row):

        temp = map(int, f.readline().strip().split(' '))
	if A==a+1:
            arregloA = temp

    B = int(f.readline().strip())

    for b in xrange(row):

        temp = map(int, f.readline().strip().split(' '))
	if B==b+1:
            arregloB = temp

    for c in arregloA:
        
        for d in arregloB:

            if c==d:
               r[t] += 1
               v[t] = c

    if r[t]==1:

        s = "Case #%d: %d" % (t+1, v[t])

    elif r[t]==0:

        s = "Case #%d: Volunteer cheated!" % (t+1)

    else:

        s = "Case #%d: Bad magician!" % (t+1)

    print s
    #o.write(s)
