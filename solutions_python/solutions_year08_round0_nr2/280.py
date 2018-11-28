#!/usr/bin/python

from optparse import OptionParser

#From string 'HH:MM' to minute from 00:00
def string2Minute(hhmm):
    hh = int(hhmm.split(':')[0])
    mm = int(hhmm.split(':')[1])
    return  hh*60 + mm

def main():
    USAGE = "usage: %prog [option]"
    parser = OptionParser(usage=USAGE)
    (options, args) = parser.parse_args()

    file_in = args[0]
    fi = file(file_in, 'r')
    N = int(fi.readline().rstrip('\n'))

    solutions = []
    for n in range(0, N):
        solution = [0, 0]
        # Unit of time, will be in minute

        #
        # Parse input
        #
        turnAround = int(fi.readline().rstrip('\n'))
        line_schedule = fi.readline().rstrip('\n')
        A2B = int(line_schedule.split(' ')[0])
        B2A = int(line_schedule.split(' ')[1])

        # Data structure in time_table
        #    (departure time, duration of trip, departure port)
        #
        time_table = []
        for i in range(0, A2B):
            line = fi.readline().rstrip('\n')
            departure_time = string2Minute(line.split(' ')[0])
            arrival_time = string2Minute(line.split(' ')[1])
            time_table.append([departure_time, arrival_time - departure_time, 'A'])

        for i in range(0, B2A):
            line = fi.readline().rstrip('\n')
            departure_time = string2Minute(line.split(' ')[0])
            arrival_time = string2Minute(line.split(' ')[1])
            time_table.append([departure_time, arrival_time - departure_time, 'B'])

        #
        # Processing
        #

        # Sort time_table by departure time
        time_table.sort(lambda x, y: cmp(x[0], y[0]))

        # portA store a time till particular train will be available at port A
        portA = []
        # portB store a time till particular train will be available at port B
        portB = []

        last_depart_time = time_table[0][0]
        for i in range(0, A2B+B2A):
            current_schedule = time_table.pop(0)
            duration4mLastDepart = current_schedule[0] - last_depart_time
            travel_time = current_schedule[1] + turnAround

            # Update time of train in expecting to arrive at both port
            for j in range(0, len(portA)):
                remaining_time = portA[j] - duration4mLastDepart
                if remaining_time <=0:
                    remaining_time =0
                portA[j] = remaining_time

            for j in range(0, len(portB)):
                remaining_time = portB[j] - duration4mLastDepart
                if remaining_time <=0:
                    remaining_time =0
                portB[j] = remaining_time

            train_available = False
            if current_schedule[2] == 'A':      # depart at port A
                if len(portA) > 0:
                    if portA[0] == 0:
                        portA.pop(0)
                        train_available = True

                if train_available == False:
                    solution[0] += 1

                # Insert train with travel_time (remain_time till available again) in portB
                # Insertion will not alter the order of train in list
                portB.append(travel_time)
                portB.sort()
            else:                               # depart at port B
                if len(portB) > 0:
                    if portB[0] == 0:
                        portB.pop(0)
                        train_available = True

                if train_available == False:
                    solution[1] += 1

                # Insert train with travel_time (remain_time till available again) in portA
                # Insertion will not alter the order of train in list
                portA.append(travel_time)
                portA.sort()

            last_depart_time = current_schedule[0]
        solutions.append(solution)

    #write output
    file_out = file_in[:len(file_in)-3] + ".out"
    fo = file(file_out, 'w')
    for n in range(0, N):
        fo.write("Case #%d: %d %d\n" %(n+1, solutions[n][0], solutions[n][1]))
    fo.close()

if __name__ == "__main__":
    main()
