ifile = "B-small-attempt2.in"
#ifile = "test-input-file-big"
  
f = open(ifile,'r')
n = (int) (f.readline()) # n of cases
n1 = 1
while (n1 <= n):
    #
    # read C(3) D(2) N(EList)
    #
    case_line = f.readline()
    case_line = case_line.split(" ")
    
    c = case_line.pop(0) # transformation triples 
    ttriples = list() 
    for i in range(int(c)):
        # base and non-base elemnts
        eset = case_line.pop(0)
        triple = [e for e in eset if e != '']
        ttriples.append(triple)
#        print ttriples
        
    d = case_line.pop(0) # opposing pairs 
    opairs = list()
    for i in range(int(d)):
        oset = case_line.pop(0)
        pair = [e for e in oset if e != '']
        opairs.append(pair)
#        print opairs

    el = case_line.pop(0) # elements
    elements = list()
    elements = [e for e in case_line[0] if e != '\n']
     
    #    
    # SOLVE
    #
    res = list() # resulting list
    for i in range(len(elements)):
        # invoke
#        print "e", elements
        # if there is already something in the list, pop that
        if (len(res) > 0):
            e1 = res.pop()       # pop 1st from res list 
            if (len(elements) < 1):
                res.append(e1) # just push back to res if have no elements
                break
            e2 = elements.pop(0) # pop 2nd from elements            
        else:
            if len(elements) < 2:
                res = elements
                break
            e1 = elements.pop(0) # pop 1st
            e2 = elements.pop(0) # pop 2nd
        
        # try to combine
        comb = [t[2] for t in ttriples if ((e1,e2) == (t[0],t[1])) or ((e2,e1) == (t[0],t[1])) ]
        if len(comb) > 0:
            res.append(comb[0])
            continue
            
        # check for opposing pair for e1
        e1o = [o[1] for o in opairs if (e1 == o[0])] or [o[0] for o in opairs if (e1 == o[1])] # opposing element to e1
#        print "e1o", e1o
        if len(e1o)> 0 and e1o[0] in res: # clear list if o.pair is already in res list
            res = []
#            print "res cl1", res
        else:
            # push to result list
            res.append(e1)
        
        # check for opposing pair for e2
        e2o = [o[1] for o in opairs if (e2 == o[0])] or [o[0] for o in opairs if (e2 == o[1])] # opposing element to e1
#        print "e1o", e1o
        if len(e2o)> 0 and e2o[0] in res: # clear list if o.pair is already in res list
            res = []
#            print "res cl2", res            
        else:
            # push to result list
            res.append(e2)

#    print n1, "resT", res        
    print "Case #%s: [%s]" % (n1, ', '.join(res))
    n1 = n1 + 1
