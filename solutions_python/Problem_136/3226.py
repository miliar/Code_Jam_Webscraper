import fileinput
import pprint

i = []
for line in fileinput.input():
    i.append(line)

test_cases = int(i.pop(0))
cases = []
while test_cases:
    line = i.pop(0)
    line = line.strip().split(" ")
    
    c = float(line[0])
    f = float(line[1])
    x = float(line[2])

    test_cases -= 1
    cases.append([c,f,x])

def cookie_clicker(c,f,x,case_number):
    cps = 2
    time = 0
    solved = False

    while not solved:

        # How long will it take us to get another farm
        seconds_until_next_farm = float(c) / cps

        # If we get another farm, it'll take us 
        seconds_until_x_if_next_farm = (float(x) / (cps + f)) + seconds_until_next_farm
        seconds_until_x_reached = float(x) / cps

        # total_time_if_nf = time + seconds_until_x_if_next_farm + seconds_until_next_farm
        # total_time_now = time + seconds_until_x_reached

        # print "total time if nf: ", total_time_if_nf
        # print "total time if now:", total_time_now
        # print

        # print "secs until farm: ",seconds_until_next_farm
        # print "secs until x:    ", seconds_until_x_reached
        # print "secs until x nf: ", seconds_until_x_if_next_farm
        # print "cookies per sec: ", cps

        # should we wait for a farm
        if seconds_until_x_if_next_farm < seconds_until_x_reached:
            # buy a farm
            cps = cps + f
            time = time + seconds_until_next_farm
        else:
            time = time + seconds_until_x_reached
            solved = True

        # print "time:",time
        # print

    return "Case #%i: %.7f" % (case_number, time)


# print cookie_clicker(500,4,2000,1)

case_number = 1
for case in cases:
    c,f,x = case

    # pprint.pprint(case)

    print cookie_clicker(c,f,x,case_number)
    case_number += 1