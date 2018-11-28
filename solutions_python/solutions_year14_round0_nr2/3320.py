

with open('B-large.in') as inp:
    with open('out.txt', 'w') as out:
        n = int(inp.readline())
        for i in range(1, n+1):
            #Parse problem
            prob = inp.readline().split(' ')
            C = float(prob[0])
            F = float(prob[1])
            X = float(prob[2])

            #Init
            k = 0
            t = 0

            Tn= C/(2+k*F) + X/ (2 + (k+1)*F)
            Tc = X/(2 + k*F)
            #While better farm, add one
            print Tn, Tc
            while Tn < Tc:
                t += C/(2+k*F)
                k += 1
                Tn= C/(2+k*F) + X/ (2 + (k+1)*F)
                Tc = X/(2 + k*F)
                
            t += X/(2+k*F)

            out.write('Case #{}: {:.7f}\n'.format(i, t))
            print 'Case #{}: {:.7f}\n'.format(i, t)