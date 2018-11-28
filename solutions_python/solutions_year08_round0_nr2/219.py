#!/usr/bin/python
available = {}
new = {}

def get_next(a_list, b_list):
    if not len(a_list):
        return "B"
    if not len(b_list):
        return "A"

    if a_list[0]['dep'] <= b_list[0]['dep']:
        return "A"
    else:
        return "B"

def find_available_train(station, time):
    for t in available[station]:
        if t['time'] <= time:
            return t
    return None

def solve(turnaround_time, lists):
    global available, new
    available["A"] = []
    available["B"] = []
    new["A"] = []
    new["B"] = []
    while len(lists["A"]) or len(lists["B"]):
        station = get_next(lists["A"], lists["B"])
        next_scheduled_train = lists[station][0]
        lists[station] = lists[station][1:]
        train = find_available_train(station, next_scheduled_train['dep'])
        if not train:
            new_train = {'station':station, 'time': next_scheduled_train['dep']}
            new[station].append(new_train)
        else:
            available[station].remove(train)
        arr_time = next_scheduled_train['arr']
        destination = "A"
        if station == "A":
            destination = "B"

        available[destination].append({'station':destination, 'time': arr_time + turnaround_time})
        available[destination].sort(key=lambda x: x['time'])
#        print "-----"
#        print available
#        print new

    return "%d %d" % (len(new["A"]), len(new["B"]))
            

def parse_test(data):
    line = 0
    turnaround_time = int(data[line])
    line = line + 1
    (num_a, num_b) = data[line].split(" ")
    line = line + 1
    num_a = int(num_a)
    num_b = int(num_b)
    a_list = []
    b_list = []
    
    for i in range(num_a):
        sched = data[line]
        (departure, arrival) =  sched.split(" ")

        dep_list = departure.split(":")
        dep_mins = 60*int(dep_list[0]) + int(dep_list[1])
        
        arr_list = arrival.split(":")
        arr_mins = 60*int(arr_list[0]) + int(arr_list[1])

        a_list.append({'dep': dep_mins, 'arr' : arr_mins})

        line = line + 1

    for i in range(num_b):
        sched = data[line]
        (departure, arrival) =  sched.split(" ")

        dep_list = departure.split(":")
        dep_mins = 60*int(dep_list[0]) + int(dep_list[1])
        
        arr_list = arrival.split(":")
        arr_mins = 60*int(arr_list[0]) + int(arr_list[1])

        b_list.append({'dep': dep_mins, 'arr' : arr_mins})

        line = line + 1
    a_list.sort(key=lambda x: x['dep'])
    b_list.sort(key=lambda x: x['dep'])
    lists = {"A": a_list, "B": b_list}
    return (line, [turnaround_time, lists]) 

def main():
    import sys
    filename = sys.argv[1]
    input = open(filename)
    data = [line.strip() for line in input.readlines()]
    num_testcases = int(data[0])
    line = 1
    for i in range(1, num_testcases+1):
        (lines, test) = parse_test(data[line:])
        #print test
        answer = apply(solve, test)
        print "Case #%d: %s" % (i, answer)
        line = line + lines
    input.close()

if __name__ == "__main__":
    main()


