import sys
import string

def moves_for_stops(stops) : 

    # current positions for B/O
    positions = { "O" : 1, "B" : 1 }
    # the last time B or O made a move
    prev_time = { "O" : 0, "B" : 0 }
    # current time
    time = 0

    for stop in stops :
        bot = stop[0]
        pos = stop[1]

        # we need to move the bot to pos and then push
        num_moves = abs(positions[bot] - pos) + 1
        positions[bot] = pos
    
        time = max(time+1, num_moves + prev_time[bot])
        prev_time[bot] = time

    return time

def solve_case(case_num, case_str) :
    row = string.split(string.strip(case_str), " ")
    num_stops = int(row[0])
    stops = []
    for pair in xrange(1, 2*num_stops+1, 2) :
        stops.append((row[pair], int(row[pair+1])))

    num_moves = moves_for_stops(stops)
    print "Case #%d: %d" % (case_num, num_moves)

data = file(sys.argv[1]).readlines()
num_cases = int(data[0])

for case in xrange(num_cases) :
    solve_case(case+1, data[case+1])
