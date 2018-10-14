"""started 09h40

"""

from math import sqrt

import psyco
psyco.full()

_debug = 0

    

def go_further_with(cur_search_engine, queries_l, index_query):

    finished = False
    while not finished:
        try:
            cur_query = queries_l[index_query]
        except IndexError:
            finished = True

        if not finished:
            if cur_query == cur_search_engine:
                finished = True

        index_query += 1
    
    return index_query - 1
    

def algo_complete(search_engines_l, queries_l):

    nb_queries = len(queries_l)


    levels_l = [] # Contains list of list of tuple(current search engine, index reached)
    cur_level = 0
    
    levels_l.append(  [(None, 0)] )
    
        
    finished = False
    while not finished:


        print '-------- starting level', cur_level
        levels_l.append([])
        prev_level = cur_level
        cur_level += 1

        print "with %d results" % len (levels_l[prev_level])
        result_d = {}

        
        for prev_search_engine, prev_index in levels_l[prev_level]:
            for search_engine in search_engines_l:
                if prev_search_engine != search_engine:
                    
                    new_index = go_further_with(search_engine, queries_l, prev_index)
                    
                    if result_d.get(search_engine, 0) <= new_index:
                        result_d[search_engine] = new_index

                    if new_index >= nb_queries:
                        if _debug:
                            for level in levels_l:
                                print level
                        return prev_level


        # optimise. For each search engine, only keep the one that went the further
        for se in result_d.keys():
            levels_l[cur_level].append( (se, result_d[se]) )

        


def solve_case(case_no, search_engines_l, queries_l):
    print "\n\n-------------- New case", case_no

    nb_search_engines = len(search_engines_l)
    nb_queries = len(queries_l)
    
    print "%d search_engines, %d queries" % (nb_search_engines, nb_queries)


    return algo_complete(search_engines_l, queries_l)

    return 999
        
            
def main(argv):

    f_out = open(argv[1].split(".")[0] + ".out", "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):
        nb_search_engines = int(fd.readline())

        search_engines_l = []
        for i in range(nb_search_engines):
            search_engines_l.append(fd.readline().strip())

        nb_queries = int(fd.readline())

        queries_l = []
        for i in range(nb_queries):
            queries_l.append(fd.readline().strip())


        
        # Have read all stuff for this case:
        f_out.write( "Case #%d: %d\n" % (case_no,
                                         solve_case(case_no, search_engines_l, queries_l)
                                         )
                     )
        f_out.flush()


    

import sys
if __name__ == "__main__":
    main(sys.argv)
