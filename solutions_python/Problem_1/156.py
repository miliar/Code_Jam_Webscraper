for case in xrange(input()):
    eng_list = []
    for eng_count in xrange(input()):
        eng_list.append( raw_input() )
    
    #~ print "engines : %s" % (str(eng_list))
    qry_list = []
    for qry_count in xrange(input()):
        qry_list.append(raw_input())

    if len(qry_list) == 0:
        print "Case #%d: %d" % ( case+1, 0 )
        continue

    #~ print "queries: %s" % (str(qry_list))
    
    # el algoritmo ....
        
    def compare(a,b):
        if  a[1] > b[1]:
            return -1
        elif a[1] < b[1]:
            return 1
        else:
            return 0
    
    result = 0
    while( len(qry_list) > 0 ):
        result += 1
        eng_performance = []
        for an_engine in eng_list:
            try:
                eng_performance.append( (an_engine,qry_list.index(an_engine)) )
            except:
                eng_performance.append( (an_engine,len(qry_list)) )
        
        #~ print "eng_performance: %s" % (eng_performance)
        eng_performance.sort( compare )
        #~ print "eng_performance (sorted): %s" % (eng_performance)
        qry_list[:eng_performance[0][1]] = []
        #~ print "qry_list (deleted): " + str(qry_list)

    #~ print result
    print "Case #%d: %d" % ( case+1, result-1 )

