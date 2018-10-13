#!/usr/bin/python
def main():

  for test_case in range(input()): #Looping through each test case
  
    srch_engs = {}
    queries = [] 
    switches = 0

    for num_srch_engs in range(input()): # read all SEs into a dictionary, initialise values to 0
      srch_engs[raw_input()] = 0

    for num_queries in range(input()): # read all queries into a list
      queries.append(raw_input())

    lowest = 99999    # keep track of the least frequently occuring query... num_queries is a good upper bound

    while (queries):  # loop will run till there are queries left

      #choose which SE is to be used 
      for query_key in srch_engs.iterkeys(): # frequency count of SEs
         qcount = queries.count(query_key)
         if (qcount  < lowest):
           lowest = qcount
    #     print qcount
         srch_engs[query_key] = qcount
      
    #  print lowest 
      
      if(lowest > 0): # check if whole shebang needs to be done at all
         for query_key, query_value in srch_engs.iteritems(): # 
           if (query_value > lowest): 
             srch_engs[query_key] = -1
         for query_key, query_value in srch_engs.iteritems(): # calculate distances
           if (int(query_value) != 0): 
             srch_engs[query_key] = queries.index(query_key)
       #  print srch_engs
         current_engine = sorted(srch_engs, key=srch_engs.__getitem__, reverse=True).pop(0)# find greatest distance 
      else:          
         current_engine = sorted(srch_engs, key=srch_engs.__getitem__ ).pop(0)# use engine with frequency 0 
      # end of choosing SE bit

      #run queries on chosen SE
      while (queries): # loop will run till there are queries left
        current_query = queries[0]
        queries.remove(current_query)
        
        if (current_query == current_engine): # check to switch SEs  before universe implosion :)
            queries.insert(0,current_query) 
            switches+=1    
            break

    print 'Case #%s: %s' % (test_case + 1,str(switches) )
main()
