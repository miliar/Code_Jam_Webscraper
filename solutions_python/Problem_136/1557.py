import sys

fname = sys.argv[1]

handler = open(fname, "r")
lines = [line.strip() for line in handler]

testcases_count = int(lines.pop(0))

for case in range(testcases_count):
    C, F, X = map(float, lines.pop(0).split(' '))
    
    time_passed = 0
    production_rate = 2.0
    best_time = sys.float_info.max
    time_to_win = 0

    while time_to_win <= best_time:
        # how long it will take to reach X with the current variables
        time_to_win = time_passed + (X / production_rate)
        
        # record a new best time
        if time_to_win < best_time: 
            best_time = time_to_win 
        
        # time to buy a new farm and accelerate the production rate
        time_passed = time_passed + C / production_rate
        production_rate = production_rate + F
        
	
    print "Case #%d: %.7f" % (case+1, best_time)
	
handler.close()