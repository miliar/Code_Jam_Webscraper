


def smooth_array(inputlist, toadd): # [0.1, 0.2, 0.3, 0.4]
    maxnumindex = 1
    inputlist = list(inputlist)
    inputlist.append(1.0) # add sentinel

    while maxnumindex < len(inputlist):
        eventual = (sum(inputlist[:maxnumindex]) + toadd) / maxnumindex
        if eventual <= inputlist[maxnumindex]:
            for index in range(maxnumindex):
                inputlist[index] = eventual
            break
        maxnumindex += 1
    return inputlist[:-1]
print(smooth_array([0.1,0.2,0.4,0.4],0.51))


with open('csmall.in') as infile:
     with open('coretraining.out','w') as outfile:
         cases = int(infile.readline())
         for casenum in range(cases):
            N, K = [int(a) for a in infile.readline().split()]
            toadd = float(infile.readline())
            numbers = [float(a) for a in infile.readline().split()]
            numbers.sort()
            resultnumbers = smooth_array(numbers,toadd)
            # fuck the large case
            result = 1.0
            for prob in resultnumbers:
             result = result * prob
            outfile.write("Case #%d: %f\n" % (casenum+1, result))

