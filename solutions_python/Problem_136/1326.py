#!/usr/bin/python3.2

filename = "B-large.in"

FILE = open(filename)
T = int(FILE.readline())


def get_time(c, f, x):
    if x == 0: return 0
    rate = 2.0
    cur_time = 0.0
    #print(c, f, x)

    while 1:
        # 2 cases, either we make it to next farm or we make it all the way to x
        time_to_win = x/rate;
        time_to_farm = c/rate;
        # if farms is an optimal solution then at least one farm must be an improvement
        time_to_win_after_farm = time_to_farm + x/(rate + f)
        if time_to_win <= time_to_farm:
            return time_to_win + cur_time
        if time_to_win <= time_to_win_after_farm:
            return time_to_win + cur_time
        else:
            cur_time += time_to_farm
            #print("building farm at time" + str(cur_time))
            rate += f



for i in range(1,T+1):
    C,F,X = [float(x) for x in FILE.readline().split()]
    time = get_time(C,F,X)
    print('Case #' + str(i) + ': ' + str(time))

