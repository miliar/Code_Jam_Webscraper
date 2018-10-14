#!/usr/bin/env python
import sys
import array

if __name__ == '__main__':
    num_case = int(sys.stdin.readline())    
    for case_n in range(num_case):
        num_engine = int(sys.stdin.readline())
        engines = []
        for n in range(num_engine):
            engines.append(sys.stdin.readline().strip())
        
        num_query = int(sys.stdin.readline())
        queries = []
        for n in range(num_query):
            queries.append(sys.stdin.readline().strip())
    
        max = 0
        max_engine = ""
        n_switch = 0
        
        rest_engines = []
        rest_engines.extend(engines)

        #if case_n+1 == 1:
        #    print engines;
        #    print queries;
        while (queries):
            for engine in rest_engines:
                try:
                    index = queries.index(engine)
                except:
                    index = -1                    
                    break
                    
                if index > max:                  
                    max = index;
                    max_engine = engine
                    
                #if case_n+1 == 1:    
                #    print engine + " %d"%index
                
             
            if index == -1:                
                break
            #print "max %s index: %d"%(max_engine,max)   
            #print max_engine+": %d"%max
            #print engines
            rest_engines = []
            rest_engines.extend(engines)
            rest_engines.remove(max_engine)
            
            
            del queries[0:max]
            #print queries
            n_switch = n_switch + 1
            max = 0
            max_engine = ""
           
        print "Case #%d: %d"%(case_n+1,n_switch)

            
    #print engines
    #print queries
    
    