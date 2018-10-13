def SelectEngine(Engines,Querys):
    index = 0
    for item in Engines:
        #check to see if the engine is not in the query, if so choose that engine
        if item not in Querys:
            return Engines.index(item)
        #choose the engine wich can accept more querys before having to switch
        if index < Querys.index(item):
            index = Querys.index(item)
            engine = item

    return Engines.index(engine)
        
if __name__ == '__main__':
    input_file = open('C:\A-large.in')
    output_file = open('C:\A-large-output.txt','w')

    count = int(input_file.readline()[:-1])
    ##print "Cases: ",count
    for x in range(count):    
        output_file.write("Case #" + str(x+1) +": ")
        
        engines_num = int(input_file.readline()[:-1])
        engine_list = []

        
        
        for y in range(engines_num):
            engine_list.append(input_file.readline()[:-1])

        
            
        querys_num = int(input_file.readline()[:-1])
        query_list = []

            
        
        for y in range(querys_num):
            query_list.append(input_file.readline()[:-1])

            
        switches = 0
        current_engine = SelectEngine(engine_list,query_list)
        current_query=0

    ##    if x == 8:
    ##        print "Engines: ",engines_num
    ##        print "     ",engine_list,"\n"
    ##        print "Querys: ",querys_num
    ##        print "     ",query_list,"\n"
    ##        print "Choosed:",engine_list[current_engine],"Engine","\n"

        unprocessed_query_list = query_list

        #process the query
        
        for item in query_list:
    ##        if x == 8:
    ##            print "Procesing query",item,"Index:",unprocessed_query_list.index(item)
            if(item == engine_list[current_engine]):
    ##            if x == 8:                
    ##                print "Query:",item,"can't go to Engine:",engine_list[current_engine]
                current_engine = SelectEngine(engine_list,unprocessed_query_list)
                switches += 1

            unprocessed_query_list = unprocessed_query_list[1:]
    ##        if x == 8:
    ##            print "Query:",item,"went to Engine:",engine_list[current_engine]       
    ##            print "Remaining querys:",unprocessed_query_list
    ##            print "Engine Index:",current_engine
    ##            print "Max Engine Index:",len(engine_list)


        output_file.write(str(switches)+"\n")

    output_file.close()
    input_file.close()            
