with open('B-large.in', 'r') as fin:
    n = int(fin.readline())
    results = []
    for i in range(n):
        line = [float(x) for x in fin.readline().split()]
        c = line[0]
        f = line[1]
        x = line[2]
        cps = 2
        cks = 0
        time = 0
        while (cks < x):
            if (x-cks < c):
                time += ((x-cks)/cps)
                cks += (x-cks)
                break
            else:
                time += (c/cps)
                cks += c
            if ((x-cks)/cps) > ((x-cks+c)/(cps+f)):
                cks -= c
                cps += f
        #print('Case #'+str(i+1)+' : '+str(time))
        results.append(time)
    with open('out.txt', 'w') as fout:
        for ind, r in enumerate(results):
            fout.write('Case #'+str(ind+1)+': '+str(r)+'\n')
