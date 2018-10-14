def trip_compare(x, y):
    if x[1]>y[1]:
       return 1
    elif x[1]==y[1]:
       return 0
    else: # x<y
       return -1
   
def numeric_compare(x, y):
    if x>y:
       return 1
    elif x==y:
       return 0
    else: # x<y
       return -1

def convert(time):
    (hour, min) = time.split(":")
    (hour, min) = (int(hour), int(min))
    return hour * 60 + min

def train(schedule):
    #(A, 10, B, 11:30)
    trains = {}
    trains["A"] = 0
    trains["B"] = 0
    stations = {}
    stations["A"] = 0
    stations["B"] = 0
    arrivals = {}
    arrivals["A"] = []
    arrivals["B"] = []
    for task in schedule:
        (src, start, desc, end) = task
        print "Schedule", src, start, desc, end
        while(len(arrivals[src]) > 0 and arrivals[src][0] <= start):
            # Update depod
            stations[src] = stations[src] + 1
            del arrivals[src][0]
            print "Train arrives at", src
        if(stations[src] == 0):
            #Create new Train
            stations[src] = stations[src] + 1
            trains[src] = trains[src] + 1
            print "Create new train at", src
        stations[src] = stations[src] - 1
        arrivals[desc].append(end)
        arrivals[desc].sort(numeric_compare)
        print "Train should arrives in",desc,"at",end
        print ""
    return (trains["A"], trains["B"])

input_file = open("input.txt")
output_file = open("output.txt", "w")
case_count = int(input_file.readline())
for i in range(1, case_count + 1):
    turnaround_time = int(input_file.readline())
    (NA, NB) = input_file.readline().strip().split(" ")
    (NA, NB) = (int(NA), int(NB))
    trips = []
    for j in range(NA):
        (start, end) = input_file.readline().strip().split(" ")
        start = convert(start)
        end = convert(end)
        end = end + turnaround_time
        trips.append(("A", start, "B", end))
    for j in range(NB):
        (start, end) = input_file.readline().strip().split(" ")
        start = convert(start)
        end = convert(end)
        end = end + turnaround_time
        trips.append(("B", start, "A", end))
        
    trips.sort(trip_compare)
    
    (trains_A, trains_B) = train(trips)
    print "=>", trips, trains_A, trains_B
    output_line = "Case #%s: %s %s\n" % (i, trains_A, trains_B)
    output_file.writelines([output_line])
    print output_line
    