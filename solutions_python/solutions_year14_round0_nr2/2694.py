# Google Jam code - Yuval Feinstein
## Ex 2 - Cookie clicker

def game(T):
    output_file = open('output.txt','w')
    INITIAL_PRODUCTION_RATE = 2
    INITIAL_COOKIES = 0
    with open(T) as input_file:
        test_cases = int(input_file.readline())
        for test in range(test_cases):
            C,F,X = [float(x) for x in input_file.readline().split(' ')]
            total_time = 0;
            production_rate = INITIAL_PRODUCTION_RATE
            best_opt = False
            while not best_opt:
                first_option = X/production_rate
                upgrade_time = C/production_rate
                production_rate += F
                second_option = X/production_rate + upgrade_time
                # checks if the upgrade is better than not upgrading
                best_opt = first_option <= second_option
                if best_opt:
                    total_time += first_option
                else:
                    total_time += upgrade_time


            output_file.write('Case #'+str(test+1) +': {0:.7f}'.format(total_time)+'\n')
    output_file.close()
                    
                
            
            
