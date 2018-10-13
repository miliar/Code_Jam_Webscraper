input_file = "large_input.in"

f = open(input_file)

def nextLine():
    line = f.readline()
    if (line.endswith("\n")):
        return line[0:-1]
    else:
        return line;

def greaterThan(num1, num2):
    x = (num1 - num2)
    if (x > 0):
        if  (x > 1*10**(-4)):
            return True
        else:
            return False
    else:
        return False


num_cases = int(nextLine())

turnaround_times = [0] * num_cases
trips_a_b = [0] * num_cases
trips_b_a = [0] * num_cases
times_a_b = [0] * num_cases
times_b_a = [0] * num_cases
times_dec_a_b = [0] * num_cases
times_dec_b_a = [0] * num_cases

def mapSplitter(x):
    return x.split(":")

def mapTimeToDecimal(x):
    sp = x.split(":")
    return float(int(sp[0]) + (float(sp[1]) / 60))

for case in range(num_cases):
    turnaround_times[case] = int(nextLine())
    trips = str(nextLine())
    trips_split = trips.split(" ")
    trips_a_b[case] = int(trips_split[0])
    trips_b_a[case] = int(trips_split[1])

##    times_a_b[case] = [0] * trips_a_b[case]
    times_dec_a_b[case] = [0] * trips_a_b[case]
    for i in range(trips_a_b[case]):
        nl = nextLine()
##        times_a_b[case][i] = map(mapSplitter, nl.split(" "))
        times_dec_a_b[case][i] = map(mapTimeToDecimal, nl.split(" "))        
        
##    times_b_a[case] = [0] * trips_b_a[case]
    times_dec_b_a[case] = [0] * trips_b_a[case]
    for i in range(trips_b_a[case]):
        nl = nextLine()
##        times_b_a[case][i] = map(mapSplitter, nl.split(" "))
        times_dec_b_a[case][i] = map(mapTimeToDecimal, nl.split(" "))
      
###################TIME TO DECIMAL##############
##
##    times_dec_a_b[case] = [0] * trips_a_b[case]
##
##    for i in range(trips_a_b[case]):
##        times_dec_a_b[case][i] = map(mapTimeToDecimal, nextLine().split(" "))
##        
##    times_dec_b_a[case] = [0] * trips_b_a[case]
##
##    for i in range(trips_b_a[case]):
##        times_dec_b_a[case][i] = map(mapTimeToDecimal, nextLine().split(" "))


##########Process INFO###########
##print times_dec_b_a[0]
        
for case in range(num_cases):
    num_trains_a = 0
    num_trains_b = 0

    departures_from_a = [0] * trips_a_b[case]
    departures_from_b = [0] * trips_b_a[case]

    for i in range(trips_a_b[case]):
        departures_from_a[i] = times_dec_a_b[case][i][0]
    for i in range(trips_b_a[case]):
        departures_from_b[i] = times_dec_b_a[case][i][0]

    arrivals_to_a = [0] * trips_b_a[case]
    arrivals_to_b = [0] * trips_a_b[case]

    for i in range(trips_a_b[case]):
        arrivals_to_b[i] = times_dec_a_b[case][i][1]
    for i in range(trips_b_a[case]):
        arrivals_to_a[i] = times_dec_b_a[case][i][1]

    departures_from_a.sort()
    departures_from_b.sort()
    arrivals_to_a.sort()
    arrivals_to_b.sort()

##    if (case == 19):
##        print departures_from_a
##        print arrivals_to_a

    for i in range(len(departures_from_a)):
        if (len(arrivals_to_a) > 0):
            if greaterThan((arrivals_to_a[0] + (float(turnaround_times[case]) / 60)), departures_from_a[i]):
                num_trains_a = num_trains_a + 1
            else:
                arrivals_to_a.pop(0)
        else:
            num_trains_a = num_trains_a + 1
            
    for i in range(len(departures_from_b)):
        if (len(arrivals_to_b) > 0):
            if greaterThan((arrivals_to_b[0] + (float(turnaround_times[case]) / 60)), departures_from_b[i]):
                num_trains_b = num_trains_b + 1
            else:
                arrivals_to_b.pop(0)
        else:
            num_trains_b = num_trains_b + 1

    
    
    print "Case #" + str(case + 1) + ": " + str(num_trains_a) + " " + str(num_trains_b);
