#!/usr/bin/env python

input = int(raw_input())
input_i = 1
while input_i <= input:

    
    num_search_engines = int(raw_input())
    search_engines = []
    i = 0
    while i < num_search_engines:
        search_engines.append(raw_input())
        i = i + 1
    
    num_search_strings = int(raw_input())
    search_strings = []
    i = 0
    while i < num_search_strings:
        search_strings.append(raw_input())
        i = i + 1

    #print '-'*40
    #for Q in search_strings:
    #    print Q
    #print '-'*40
    #
    
    switches = 0
    set_search_engines = set([])
    taken = 0
    first_time = 1
    
    for Q in search_strings:    
        if Q in set_search_engines:
            pass
        else:
            
            set_search_engines.add(Q)
            taken += 1
            #for s in set_search_strings: print s,
            #print set_search_engines
            # The last search string is the desired search engine to get all
            # the search strings

            if taken == len(search_engines):
                switches += 1
                set_search_engines.clear()
                set_search_engines.add(Q)
                taken = 1
    
    print 'Case #%d: %d' % (input_i, switches)
    input_i += 1