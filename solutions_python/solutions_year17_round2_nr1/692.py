import sys

def get_ints(line):
    space = line.find(' ')
    return [int(line[:space]), int(line[space:])]


#passes in start point then speed
def get_end_time(horse, destination):
    length = destination-horse[0]
    return length*1.0/horse[1]

def get_largest_end_time(horses, destination):   
    largest = get_end_time(horses[0], destination)

    for i in range(1,len(horses)):
        end_time = get_end_time(horses[i], destination)
    
        if end_time > largest:
            largest = end_time
    return largest

def solution(horses, destination):
    time = get_largest_end_time(horses, destination)

    return str(destination*1.0/time)

in_file = sys.argv[1]
in_stream = open(in_file)
lines = in_stream.readlines()

i = 1
case_num = 1
while i < len(lines):
    values = get_ints(lines[i])
    num_horses = values[1]
    d = values[0]
    horses = []
    for j in range(num_horses):
        horses.append(get_ints(lines[i+j+1]))
    print "Case #%d: "%case_num + solution(horses, d)
    i += num_horses+1
    case_num += 1
    
        
