#!/usr/bin/env python
""" """
import sys

def analyse_test_case(P,pR):
    
    def minBribes(bribes, options, breaks, lev) :
        res = []
        #print(lev +"%s %s %s" %(str(bribes),str(options),str(breaks)))
        for opt in options :
            #determining bribes for realeasing prinser opt
            k = 0
            CellRealease = opt
            while not ((breaks[k] < CellRealease) and (CellRealease < breaks[k+1])) :
                k = k + 1
                
            #while breaks[k+1] < CellRealease and k < len(breaks)-1 :
            #    k = k + 1
            bribes_pris = breaks[k+1] - breaks[k] - 2
            #print(lev + 'bribes to realease %i = %i' %(opt,bribes_pris) + ' bound[%i %i]' % (breaks[k], breaks[k+1]))
            bribes_k = bribes + bribes_pris

            if len(options) > 1 :
                breaksNew = breaks + [opt]
                breaksNew.sort()
                optNew = [pris for pris in options if pris <> opt]
                res.append( minBribes(bribes_k, optNew, breaksNew, lev + '  '))
            else :
                return bribes_k
        #print(lev +str(res))
        return min(res)

    return minBribes(0,pR,[0,P+1],'  ')

def analyse_datafile(datafile):
    f = file(datafile)
    lines = f.readlines()
    f.close()
    N = int(lines[0].strip())
    print('file "%s" contains %i cases' % (datafile,N))
    cases = []
    i_ind = 1
    for i in range(N) :
        P,Q = [int(c) for c in lines[i_ind].strip().split(' ')]
        pR = [int(c) for c in lines[i_ind+1].strip().split(' ')]
        print(P,pR)
        cases.append([P,pR])
        i_ind = i_ind + 2
    output = []
    print('\nanalysing cases')
    count = 1 
    for case in cases :
        bribes = analyse_test_case(case[0],case[1])
        output.append("Case #%i: %i" % (count,bribes))
        print(output[-1])
        count = count + 1
    return output


output =  analyse_datafile(sys.argv[1])

fout = file(sys.argv[1]+'_output','w')
fout.write('\n'.join(output))
fout.close()
