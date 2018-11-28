# greedy!

def parse_time_to_mins(timestr):
    hour, mins = map(int, timestr.split(':'))
    return hour * 60 + mins

if __name__ == '__main__':
    N = int(raw_input())
    for x in range(N):
        turnaround = int(raw_input())
        NA, NB = map(int, raw_input().split())
        tripsA, tripsB = [], []
        tripsA_start, tripsB_start = [], []
        
        for na in range(NA):
            start, end = map(parse_time_to_mins,
                             raw_input().split(' '))
            tripsA.append( (end, start) ) # note: END, start
            tripsA_start.append( (start, end) )
        for nb in range(NB):
            start, end = map(parse_time_to_mins,
                             raw_input().split(' '))
            tripsB.append( (end, start) )
            tripsB_start.append( (start, end) )

        tripsA.sort()
        tripsB.sort()
        tripsA_start.sort()
        tripsB_start.sort()

        #print 'TripsA:', tripsA_start
        #print 'TripsB:', tripsB_start
        #print 'turnaround', turnaround

        a_free_start = [True] * len(tripsA)
        b_free_start = [True] * len(tripsB)

        b_start_index = 0
        #print 'tripA...'
        for aEnd, aStart in tripsA:
            while b_start_index < len(tripsB):
                b_start = tripsB_start[b_start_index][0]
                #print aEnd, 'against', b_start
                if b_free_start[b_start_index] and aEnd+turnaround <= b_start:
                    b_free_start[b_start_index] = False
                    break
                b_start_index += 1
            if b_start_index == len(tripsB):
                break

        a_start_index = 0
        #print 'tripB...'
        for bEnd, bStart in tripsB:
            while a_start_index < len(tripsA):
                a_start = tripsA_start[a_start_index][0]
                #print bEnd, 'against', a_start
                if a_free_start[a_start_index] and bEnd+turnaround <= a_start:
                    a_free_start[a_start_index] = False
                    break
                a_start_index += 1
            if a_start_index == len(tripsA):
                break

        #print a_free_start
        #print b_free_start
        print "Case #%d: %d %d" % (x+1,
                                   a_free_start.count(True),
                                   b_free_start.count(True))
        
