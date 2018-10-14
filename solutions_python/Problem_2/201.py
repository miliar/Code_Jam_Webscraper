def convert_to_minutes(s):
    """Convert from 'HH:MM' format to integer MMMM format"""
    
    hour, minute = s.split(':')
    return int(hour)*60 + int(minute)


def process_one_shedule_line(line, T, from_shedule, to_shedule):
    """Process one line of shedule and add results to 'shedule lists'"""
    
    line=line.replace('\n', '')
    data=line.split(' ')
    
    time_from = convert_to_minutes(data[0])
    time_to = convert_to_minutes(data[1]) + T
            
    from_shedule.append((time_from, True))
    to_shedule.append((time_to, False))
    

def calc_train_needs(shedule):
    """Process shedule list and calculate how many trains needed"""

    cur_trains = initial_trains = 0
    for x in shedule:
        # Train arrives
        if x[1] == False: cur_trains += 1; continue
        
        # So, train leaves the station
        if cur_trains == 0: 
            initial_trains +=1
        else:
            cur_trains -= 1

    return initial_trains

def process_data_files(fin, fout):
    """Read input data from 'fin' and write results into 'fout'"""

    N = int(fin.readline())
    

    for i in xrange(N):
        
        # Shedules in station A and B.
        # Contain only times of departures and arrivals on the station.
        # Each record is tuple and contains time_in_minutes and boolean value
        # (True, if the train leaves the station and False, if the thain arrivals)
        # So, sorting this lists is a very simple operation
        A_shedule=[]
        B_shedule=[]

        T = int(fin.readline())
        data=fin.readline().split(' ')
        NA, NB = int(data[0]), int(data[1])

        for shedule in xrange(NA):
            process_one_shedule_line(fin.readline(), T, A_shedule, B_shedule)

        for shedule in xrange(NB):
            process_one_shedule_line(fin.readline(), T, B_shedule, A_shedule)

        A_shedule.sort()
        B_shedule.sort()


        fout.write("Case #%d: %d %d\n" % 
                   (i+1, calc_train_needs(A_shedule), calc_train_needs(B_shedule)))
