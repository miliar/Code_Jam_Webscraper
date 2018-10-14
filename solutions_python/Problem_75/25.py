with open('input2.txt', 'r') as fin:
    with open('output2.txt', 'w') as fout:
        numcases = int(fin.readline())
        for i in range(1,numcases+1):
            line = fin.readline().split()
            iterator = line.__iter__()
            C = int(next(iterator))
            combs = []
            for j in range(C):
                x = next(iterator)
                combs.append((x[0:2], x[2]))
            D = int(next(iterator))
            opps = []
            for j in range(D):
                opps.append(next(iterator))

            numchars = next(iterator)
            chars = next(iterator)
            result = []


            for j in chars:
                result.append(j)
                if len(result) > 1:
                    for k in combs:
                        if (result[-1] in k[0] and result[-2] in k[0] and ((result[-1] != result[-2]) or (k[0][0] == k[0][1]))):
                            result = result[:-2] + [k[1]]
                            break
                    else:
                        for k in opps:
                            for m in range(len(result)-1):
                                if (result[-1] in k and result[m] in k and (result[-1] != result[m])):
                                    result = []
                                    break
            fout.write("Case #"+str(i)+": [")
            for j in range(len(result)-1):
                fout.write(result[j]+', ')
            if (len(result) > 0):
                fout.write(result[-1])

            fout.write(']\n')
