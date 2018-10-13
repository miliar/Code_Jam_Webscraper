
for T in range(1, input()+1):
    C, F, X = (float(x) for x in raw_input().split())
    cur_output = 2
    cur_time = 0
    while X/(cur_output+F) > C/F:
        # buy a farm
        cur_time += C/cur_output
        cur_output += F
    cur_time += X/cur_output
    print "Case #" + str(T) + ": " + str(cur_time)