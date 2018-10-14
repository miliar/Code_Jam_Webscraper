
# A function to add the time
# to a given number
def at(time, mins):
    while mins >= 60:
        time+=100
        mins -= 60

    time += mins
    if time%100 >= 60:
        time+=40

    return time
        
# Notation
# arrival - 0
# departure - 1
# We are doing this since, we want
# arrival event to be processed before
# departure
# A-> 0
# B -> 1

def ptt(t):
    ''' Process the time table given as a list of
        tuples in T, and returns min no. of trains
        at A and B'''

    # min a min b is stored in a list
    min = [0, 0]

    # current status (trains needed) at each station
    status = [0, 0]

    for (train, dir, station) in t:
        if dir == 1:
            # print "Train leaving stations %s"%(["a","b"][station])
            status[station] -= 1
            # print "Status is ", status
            if status[station] < min[station]:
                min[station] = status[station]
                # print "Min is ", min

        elif dir == 0:
            # print "Train arriving at station %s"%(["a","b"][station])
            status[station]+=1
            # print "Status is ", status

        # print ""


    return (-min[0], -min[1])

def parse_line(s, station, turnaround):
    times = s.split(" ")
    times = [int(time.replace(":", "")) for time in times] 
    # print times
    return [ (times[0], 1, station),  (at(times[1],turnaround), 0, (1-station)) ]


if __name__ == '__main__':

    test_cases = int(raw_input())
    for case in range(test_cases):

        tdata = []

        turntime = int(raw_input())
        [na, nb] = [int(e) for e in (raw_input().strip().split(" "))]
        
        for a in range(na):
            tdata.extend(parse_line(raw_input().strip(), 0, turntime))

        for b in range(nb):
            tdata.extend(parse_line(raw_input().strip(), 1, turntime))

        tdata.sort()
        (mina, minb) = ptt(tdata)
        print "Case #%d: %d %d"%(case+1, mina, minb) 

