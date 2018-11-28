'''
Created on Apr 12, 2014

@author: rakesh
'''


def process_test_case(i, fh):
    t = fh.readline()
    c, f, x = float(t.split()[0]), float(t.split()[1]), float(t.split()[2])
    #print c, f, x
    
    #Use the strategy
    
    #Initialize rate and cookies
    current_cookies_per_second = 2.0
    current_accumulated_cookies = 0.0
    total_time_spent = 0.0
    
    
     
    while True:
        #How many more seconds will it be if we didn't buy any more forms
        more_seconds_no_farm = (x - current_accumulated_cookies) / current_cookies_per_second
        
        #How many more seconds will it be if we did buy one more farm
        more_seconds_with_farm = (x - (current_accumulated_cookies - c)) / (current_cookies_per_second + f)
        
        #print "more_seconds_no_farm:", more_seconds_no_farm
        #print "more_seconds_with_farm:", more_seconds_with_farm

        if more_seconds_no_farm > more_seconds_with_farm:
            #print 'will buy a farm'
            
            #Do I have enough money to buy a farm?
            if current_accumulated_cookies >= c:
                #print 'Can buy a farm and going to buy it now'
                
                #First pay for it
                current_accumulated_cookies = current_accumulated_cookies - c
                
                #The rate bumps up
                current_cookies_per_second = current_cookies_per_second + f
                
            else:
                #print 'Cannot buy a farm, hence going to accumulate some cookies until I can'
                #How many more cookies do I need, until I can buy a farm, so those many additional seconds...
                more_cookies_needed = c - current_accumulated_cookies
                
                #How long will it take?
                more_seconds = more_cookies_needed / current_cookies_per_second
                
                #Calculate the time???
                total_time_spent = total_time_spent + more_seconds               
                
                #Accumulate cookies
                current_accumulated_cookies = current_accumulated_cookies + more_cookies_needed                        
        else:
            #print 'wont buy a farm'
            
            #Don't need to buy that next farm, just accumulate cookies
            current_accumulated_cookies = current_accumulated_cookies + current_cookies_per_second
            
            #Update time
            total_time_spent = total_time_spent + more_seconds_no_farm
            break
        
    case_num = "Case #"+str(i+1)+":"
    print case_num, '%.7f' % total_time_spent

    

if __name__ == '__main__':
    
    fh = open("B-large.in", "r")
    
    num_test_cases = int(fh.readline().split()[0])
    #print "Number of test cases", num_test_cases
    
    #Go through each test-case and prcocess them
    for i in range(num_test_cases):
        process_test_case(i ,fh)
        
    fh.close()