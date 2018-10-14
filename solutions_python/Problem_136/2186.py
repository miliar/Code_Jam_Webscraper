no_of_tests = int(raw_input())
for i in range(1, no_of_tests + 1):
    #first get 1st cordinate
    row1 = (raw_input())
    options1 = (row1.rsplit(" "))
    c = float(options1[0])
    f = float(options1[1])
    x = float(options1[2])
    loop = True
    results = []
    #have a farm cost
    farm_cost = c/2
    #initial estitmate without buying farm, gets updated to just collect from there
    guess = x/2
    results.append(guess)
    #initial rate
    rate = 2 + f
    #time taken
   # i = 0
    final_cost = farm_cost + x/rate
    results.append(final_cost)
    while(loop == True):
        if (final_cost >= guess):
            #if results == None:
            #    print "Case #" + str(i) + ":" + " " + str()
            print "Case #" + str(i) + ":" + " " + str(results[len(results) - 2])
            loop = False
            #success
        else:
            guess = final_cost
            farm_cost = farm_cost + (c/rate)
            rate = rate + f
            final_cost = farm_cost + (x/rate)
            results.append(final_cost)
            #print "Fianl cost is " + str(final_cost)
            #guess = final_cost
            
        
           
            
        
        
        
        
        
        
    
    
                
                       
                       
    
            
