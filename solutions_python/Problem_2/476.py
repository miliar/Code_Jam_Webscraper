

def solve_case(turnaround, trips):
    a_trains = []
    b_trains = []
    num_a = 0
    num_b = 0
    trips.sort()
    for trip in trips:
        if trip[2] == 'a':
            b_trains.append(trip[1] + turnaround)
            b_trains.sort()
            if len(a_trains) and a_trains[0] <= trip[0]:
                a_trains = a_trains[1:]
            else:
                num_a += 1
        if trip[2] == 'b':
            a_trains.append(trip[1] + turnaround)
            a_trains.sort()
            if len(b_trains) and b_trains[0] <= trip[0]:
                b_trains = b_trains[1:]
            else:
                num_b += 1
    return num_a, num_b

def solve(filename, output):
    lines = file(filename).readlines()
    out = file(output, 'w')
    num_cases = int(lines[0])
    index = 1
    for i in xrange(num_cases):
        trips = []
        turnaround = int(lines[index])
        index += 1
        NA, NB = map(int,lines[index].split(' '))
        index += 1
        for j in xrange(NA):
            dep_time = int(lines[index].split(' ')[0].split(':')[1]) + (60 * int(lines[index].split(' ')[0].split(':')[0]))
            arr_time = int(lines[index].split(' ')[1].split(':')[1]) + (60 * int(lines[index].split(' ')[1].split(':')[0]))
            trips.append([dep_time, arr_time, 'a'])
            index += 1
        for j in xrange(NB):
            dep_time = int(lines[index].split(' ')[0].split(':')[1]) + (60 * int(lines[index].split(' ')[0].split(':')[0]))
            arr_time = int(lines[index].split(' ')[1].split(':')[1]) + (60 * int(lines[index].split(' ')[1].split(':')[0]))
            trips.append([dep_time, arr_time, 'b'])
            index += 1
        res = solve_case(turnaround, trips)
        out.write("Case #%i: %i %i\n" % (i + 1, res[0], res[1]))


import sys
solve(sys.argv[1],sys.argv[2])

            
        
        
