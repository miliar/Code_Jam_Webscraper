import sys

lines = [line.strip() for line in open(sys.argv[1])]
output_file = open( "sub-9.out", "w" )

testcases = int(lines[0])

for t in range(1, testcases + 1):
    c,f,x = map(float, lines[t].split())
    cumulative_catchup_time = 0.0
    cumulative_cost = 0.0
    cumulative_time = 0.0
    past_cumulative_time = x / 2.0
    
    i = 0
    while(True):
        final_rate = 2.0 + f*i
        final_time = x / final_rate
        
        cumulative_time = cumulative_catchup_time + final_time
        
        if(cumulative_time > past_cumulative_time):
            break;
        else:
            past_cumulative_time = cumulative_time
        
        cumulative_catchup_time += c / final_rate
        i += 1
        

    result = "Case #%d: %1.7f" % (t, past_cumulative_time)
        
    output_file.write(result + "\n")
    print(result)
    
output_file.close()