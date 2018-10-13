f = open("B-small-attempt3.in","r")
fout = open("b-small.out","w")
cases = int(f.next())
for case in range(cases):

    #input
    raw = f.next().strip().split(' ')
    #print "raw:",raw
    combine = dict()
    C = int(raw[0])
    triplets = raw[1:C+1]
    print "triplets:", triplets
    for triplet in triplets:
        combine[triplet[0:2]] = triplet[2]
        combine[triplet[1]+triplet[0]] = triplet[2]
    #print "combine:",combine
    oppose = dict()
    D = int(raw[C+1])
    doublets = raw[C+2:C+2+D]
    print "doublets:", doublets
    for doublet in doublets:
        oppose[doublet[0]] = doublet[1]
        oppose[doublet[1]] = doublet[0]
    N = int(raw[C+D+2])
    invocation = raw[-1]
    print "invocation:", invocation

    #output
    outlist = []
    outdict = dict()
    for i in range(len(invocation)):
        this = invocation[i]
        if len(outlist) == 0:
            outlist.append(this)
            outdict[this] = 1
            #print "outlist:",outlist
        else:
            last = outlist[-1]
            if combine.has_key(last+this):
                outdict[last] = outdict[last] - 1
                if outdict[last] == 0:
                    del outdict[last]
                outlist[-1] = combine[last+this]
                #print "outlist:",outlist
            elif oppose.has_key(this) and outdict.has_key(oppose[this]):
                    outdict.clear()
                    outlist = []
                    #print "outlist",outlist
            else:
                outlist.append(this)
                if outdict.has_key(this):
                    outdict[this] = outdict[this] + 1
                else:
                    outdict[this] = 1
                #print "outlist",outlist
    print "outlist:",outlist,"\n\n"
    fout.write("Case #%d: [" % (case + 1))
    for i in range(len(outlist)-1):
        fout.write("%s, " % (outlist[i]))
    if len(outlist) > 0:
        fout.write(outlist[-1])
    fout.write("]")
    if case != cases-1:
        fout.write("\n")
f.close()
fout.close()
