import sys

def main(args = []):
    inf = open(args[1])


    line = inf.readline()

    num_cases = int(line)

    for i in range(num_cases):
        line = inf.readline()
        num_search_engines = int(line)

        search_engines = []
        search_engine_in_query_count = {}
        for s in range(num_search_engines):
            search_engine = inf.readline()
            search_engines = search_engines + [search_engine]
            search_engine_in_query_count[search_engine] = 0

        line = inf.readline()
        num_queries = int(line)

        queries = []
        queries_count = {}

        for q in range(num_queries):
            query = inf.readline()
            queries = queries + [query]
            if search_engine_in_query_count.has_key(query):
                search_engine_in_query_count[query] = search_engine_in_query_count[query]+1

            if queries_count.has_key(query):
                queries_count[query] = queries_count[query] + 1
            else:
                queries_count[query]=0

        case_done = 0
        
        for s in search_engine_in_query_count:
            if search_engine_in_query_count[s]==0:
                case_done = 1
                solution=0
                break

        if case_done:
            i1 = i+1
            print "Case #"+str(i1) + ": " + str(solution)
            continue


        for s in search_engine_in_query_count:
            search_engine_in_query_count[s] = 0
            
        num_switches=0
        for q in queries:
            ## Keep a running tally of which search engines are being used
            if search_engine_in_query_count.has_key(q):
                search_engine_in_query_count[q] = search_engine_in_query_count[q]+1

            no_zeroes = 1

            for s in search_engine_in_query_count:
                if search_engine_in_query_count[s]==0:
                    no_zeroes=0
                    break

            if no_zeroes:
                ## We need to do a search engine switch to the current query
                ## because all search engines are invalid otherwise
                num_switches = num_switches+1

                ## We reset all search engines and repeat the process
                for s in search_engine_in_query_count:
                    search_engine_in_query_count[s] = 0                
                
                if search_engine_in_query_count.has_key(q):
                    search_engine_in_query_count[q] = search_engine_in_query_count[q]+1         
        i1 = i+1
        print "Case #"+str(i1) + ": " + str(num_switches) 
            

if __name__=="__main__":
    main(sys.argv)
