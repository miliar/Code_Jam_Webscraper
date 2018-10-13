def compute_list(keylist, valuelist, repdict, seq):
    #print keylist, valuelist, seq
    seqlist = []
    
    for element in seq:
        prev_element = seqlist[-1] if len(seqlist) else None
        try:
            val = keylist.index((prev_element,element))
            value = valuelist[val]
            seqlist = seqlist[:-1]
            seqlist.append(value)
        except ValueError:
            rep_val = repdict.get(element,None)
            if rep_val and rep_val in seqlist:
                seqlist = []
            else:
                seqlist.append(element)
    return seqlist




def test_cases():
    with open("p3.txt") as f:
        size = f.readline()
        print 'size=%s'%size
        for i,line in enumerate(f):
            inp = line.split()
            lencomp = int(inp[0])
            comp = inp[1:lencomp+1]
            lenrep = int(inp[lencomp+1])
            rep = inp[lencomp+2:lencomp+lenrep+2]
            seq = inp[-1]
            
            keylist = []
            valuelist = []
            for el in comp:
                keylist.append((el[0],el[1]))
                keylist.append((el[1],el[0]))
                
                valuelist.append(el[2])
                valuelist.append(el[2])

            repdict = {}
            for el in rep:
                repdict[el[0]] = el[1]
                repdict[el[1]] = el[0]
            
            print "Case #%s: [%s]"%(i+1,(", ").join(compute_list(keylist, valuelist, repdict, seq)))
test_cases()
