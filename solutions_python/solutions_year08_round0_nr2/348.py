def convtimetomin(time):
    segs = time.split(":")
    mins = int(segs[1])
    mins = mins + int(segs[0]) * 60
    return mins

def solve(dataset):
    datafile = open(dataset, 'r')
    outfile = open("c:/temp/results.txt",'w')
    
    numberoftestcases = int(datafile.readline().strip())
    print "Number of Test Cases = %d" % (numberoftestcases)
    for testcasenumber in range(1,numberoftestcases+1):
        print "Test case #%d" % (testcasenumber)

        trainturnaroundtime = int(datafile.readline().strip())
        print "trainturnaroundtime: %d" % (trainturnaroundtime)

        nanb = datafile.readline().strip().split()
        na = int(nanb[0])
        nb = int(nanb[1])

        print "na = %d, nb = %d" % (na,nb)

        a_to_b_trips = []
        b_to_a_trips = []

        for i in xrange(0, na):
            times = datafile.readline().strip().split()
            departure = convtimetomin(times[0])
            arrival = convtimetomin(times[1])
            if arrival < departure:
                print "Train departing after it arrives"
            trip = (departure, arrival)
            a_to_b_trips.append( trip )
        
        for i in xrange(0, nb):
            times = datafile.readline().strip().split()
            departure = convtimetomin(times[0])
            arrival = convtimetomin(times[1])
            if arrival < departure:
                print "Train departing after it arrives"
            trip = (departure, arrival)
            b_to_a_trips.append( trip )            
        
        print "a->b: %s" % repr(a_to_b_trips)
        print "b->a: %s" % repr(b_to_a_trips)

        answer = solvecase(trainturnaroundtime, a_to_b_trips, b_to_a_trips)

        answerline = "Case #%d: %d %d" % (testcasenumber, answer[0], answer[1])
        print answerline
        outfile.write("%s\n" % answerline)

def solvecase(trainturnaroundtime, abtrips, batrips):
    departing_from_a = {}
    departing_from_b = {}

    for departure,arrival in abtrips:
        if departure not in departing_from_a:
            departing_from_a[departure] = []            
        departing_from_a[departure].append(arrival)

    for departure,arrival in batrips:
        if departure not in departing_from_b:
            departing_from_b[departure] = []   
        departing_from_b[departure].append(arrival)
    
    numstartata = 0
    numstartatb = 0

    numata = 0
    numatb = 0

    num_a_ready_at_time = {}
    num_b_ready_at_time = {}

    endofday = 24*60
    for current_minute in xrange(0, endofday+1):
        #reclaim trains ready to run again
        if num_a_ready_at_time.has_key(current_minute):
            numata = numata + num_a_ready_at_time[current_minute]
            del num_a_ready_at_time[current_minute]

        if num_b_ready_at_time.has_key(current_minute):
            numatb = numatb + num_b_ready_at_time[current_minute]
            del num_b_ready_at_time[current_minute]

        #see if we have enough trains to satisfy
        if current_minute in departing_from_a:
            departing_now_from_a = departing_from_a[current_minute]
            if len(departing_now_from_a) > numata:
                numstartata = numstartata + (len(departing_now_from_a) - numata)
                numata = len(departing_now_from_a)

            numata = numata - len(departing_now_from_a)

            for arrival_at_b_time in departing_now_from_a:
                ready_at_time = arrival_at_b_time + trainturnaroundtime
                if ready_at_time not in num_b_ready_at_time:
                    num_b_ready_at_time[ready_at_time] = 0
                num_b_ready_at_time[ready_at_time] = num_b_ready_at_time[ready_at_time] + 1


        if current_minute in departing_from_b:
            departing_now_from_b = departing_from_b[current_minute]
            if len(departing_now_from_b) > numatb:
                numstartatb = numstartatb + (len(departing_now_from_b) - numatb)
                numatb = len(departing_now_from_b)

            numatb = numatb - len(departing_now_from_b)

            for arrival_at_a_time in departing_now_from_b:
                ready_at_time = arrival_at_a_time + trainturnaroundtime
                if ready_at_time not in num_a_ready_at_time:
                    num_a_ready_at_time[ready_at_time] = 0
                num_a_ready_at_time[ready_at_time] = num_a_ready_at_time[ready_at_time] + 1


    
    return (numstartata,numstartatb)
