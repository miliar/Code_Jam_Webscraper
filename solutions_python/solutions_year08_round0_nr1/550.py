import math
import random

file = open("A-large.in")
out=open('thelarge.txt', 'w')

cases = 0

num_engines = -1
num_queries = -1

engines = []
queries = []

line_num = 0
interesting_line = 1
case_counter = 1

eng_mode = False

try:
    for line in file:
        if line_num == 0:
            cases = eval(line)

        if len(queries) < num_queries:
            queries.append(line.strip())    
 
        if line_num > 0 and len(queries)==0 and num_queries == -1 and len(engines)==num_engines:
            num_queries = eval(line)

        if len(engines) < num_engines:
            engines.append(line.strip())

        if line_num > 0 and len(engines)==0 and num_engines == -1:
            num_engines = eval(line)
        

        if num_engines==len(engines) and num_queries==len(queries):
            print 'Case', str(case_counter)
            print 'engines', engines
            print 'queries', queries
            
            keep_engines = list(engines)
            
            #print keep_engines
            
            #print 'Looking now'
            c=0
            for query in queries:
                print 'query', query
                
                for engine in keep_engines:
                    if query == engine:
                        keep_engines.remove(query)
                        
                    
                if len(keep_engines) == 0:
                    print '------------------changing engines'
                    c += 1
                    keep_engines = list(engines)
                    keep_engines.remove(query)
                    
            print c    
            
            out.write("Case #" + str(case_counter) + ": " + str(c) + "\n")
            case_counter += 1
            
            #reset       
            num_engines = -1
            num_queries = -1
            engines = []
            queries = []

        
        line_num += 1
        
    print 'cases', cases

finally:
    file.close()
    out.close();
