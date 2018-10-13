import sys
def time_to_int(str):
    f = str.split(":")
    h = int(f[0])
    m = int(f[1])
    time = h*60 + m
    return time
def count_joint(arrival_list, start_list):
    a_index = 0
    s_index = 0
    arrival_list.sort()
    start_list.sort()
    joint_count = 0
    while a_index < len(arrival_list)  and s_index < len(start_list):
        arrival = arrival_list[a_index]
        start = start_list[s_index]
        if arrival > start:
            s_index += 1
            continue
        else:
            s_index += 1
            a_index += 1
            joint_count += 1
    return joint_count
def analyse(r1):
    line = r1.readline()
    turn_around_time = int(line)
    line = r1.readline()
    from_a_num = int(line.split(" ")[0])
    from_b_num = int(line.split(" ")[1])
    a_list = []
    b_list = []
    arrival_a_list = []
    arrival_b_list = []
    start_a_list = []
    start_b_list = []
    for x in xrange(from_a_num):
        
        line = r1.readline()
        f = line.split(" ")
        start_time = time_to_int(f[0])
        arrival_time = time_to_int(f[1]) + turn_around_time
        
        start_a_list.append(start_time)
        arrival_b_list.append(arrival_time)

        #a_list.append(line)
        pass
    for x in xrange(from_b_num):
        line = r1.readline()
        f = line.split(" ")
        start_time = time_to_int(f[0])
        arrival_time = time_to_int(f[1]) + turn_around_time
        
        start_b_list.append(start_time)
        arrival_a_list.append(arrival_time)
        

        pass
    a_minus = count_joint(arrival_a_list, start_a_list)
    b_minus = count_joint(arrival_b_list, start_b_list)
    from_a = from_a_num - a_minus
    from_b = from_b_num - b_minus
    return  "%d %d"%(from_a, from_b)
    
    

def main():
    r1 = open(sys.argv[1])
    line = r1.readline()
    case_num = int(line)
    for x in xrange(case_num):
        str = analyse(r1)
        print "Case #%d: %s"%(x+1, str)
main()

