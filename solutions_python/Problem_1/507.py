import sys
sys.stdout=open('b.txt', 'w')
infile=open('A-large.in')
nooftestcases=int((infile.readline()).rstrip())
#print "No of Test Cases: "+str(nooftestcases)
i=0
while i<nooftestcases :
        #Input Sequence
        noofsearch=int((infile.readline()).rstrip())
        #print "No of Search Engines: " + str(noofsearch)
        searchdict={}
        j=0
        while j<noofsearch :
                searchdict[(infile.readline()).rstrip()] = 0
                j+=1
        #for x in searchdict :
        #       print x
        noofqueries=int((infile.readline()).rstrip())   
        #print "No of Queries: " + str(noofqueries)
        querylist=[]
        k=0
        while k<noofqueries :   
                querylist.append((infile.readline()).rstrip())
                k+=1
        #for x in querylist :
                #print x
                
        # Program Logic Begins
        querylist.reverse()
        lastsearch=searchdict.copy()
        switch=0
        while querylist != [] :
                query=querylist.pop()
                beforeswitch=''
                if len(lastsearch)==1 :
                        beforeswitch=(lastsearch.keys())[0]
                if lastsearch.has_key(query) :
                        del lastsearch[query]
                if lastsearch=={} :
                        switch+=1
                        lastsearch=searchdict.copy()
                        del lastsearch[beforeswitch]
        print 'Case #'+str(i+1)+': '+str(switch)
        i+=1
