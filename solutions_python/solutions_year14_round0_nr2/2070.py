fi = open("B-large.in")
fo = open("output_two.out", "w")

num_cases = (int)(fi.readline())

def time_to_win(C, F, X, rate):
    
    time = 0
    while(True):
        time_to_win = X / rate
        time_to_buy_farm = C / rate
        time_needed_after_buy = X / (rate+F) # linear aproximation
        if((time_to_buy_farm+time_needed_after_buy) < time_to_win):
            time += time_to_buy_farm
            rate += F
        else:
            time += time_to_win
            break
        
    return time
    
for i in range(num_cases):
    rate = 2
    line = fi.readline().rstrip().split(' ')
    line = [(float)(x) for x in line]
    C = line[0]
    F = line[1]
    X = line[2]
    time = time_to_win(C, F, X, rate)
    fo.write("Case #" + str(i+1) + ": " + "{0:.7f}".format(time) + "\n")

fo.close()
fi.close()
