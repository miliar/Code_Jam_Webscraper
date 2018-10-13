import sys

class Time:
    def __init__(self, time_str):
        self.hour = int(time_str.split(":")[0])
        self.min = int(time_str.split(":")[1])
        
    def __add__(self, other):
        t = Time(self.__str__())
        t.min += other
        if t.min >= 60:
            t.min -= 60
            t.hour += 1
        return t

    def __cmp__(self, other):
        if self.hour < other.hour:
            return -1
        elif self.hour > other.hour:
            return 1
        elif self.min < other.min:
            return -1
        elif self.min > other.min:
            return 1
        else:
            return 0
    def __str__(self):
        return "%02d:%02d" % (self.hour, self.min)

def find_longest_trip(time, turnaround, table1, table2):
    max_trip = list()
    index = 0
    for dtime,atime in table1:
        if (time + turnaround) <= dtime:
            trip = [(dtime, atime),]
            trip.extend(find_longest_trip(atime, turnaround, table2, table1[index:]))
            if len(trip) > len(max_trip):
                max_trip = trip
        index += 1
    return max_trip
            
        

def analyse_case(input_file):
    turnaround = int(input_file.readline())
    temp = input_file.readline()
    NA = int(temp.split()[0])
    NB = int(temp.split()[1])
    table = []
    for i in range(NA + NB):
        line = input_file.readline()
        dtime = Time(line.split()[0])
        atime = Time(line.split()[1])
        table.append((dtime, atime))
    tableA = table[:NA]
    tableB = table[NA:]
    if len(tableA) != NA or len(tableB) != NB:
        print "Error!"
        sys.exit()
    if NA * NB == 0:
        return (NA, NB)
    tableA.sort(lambda x,y : cmp(x[0], y[0]))
    tableB.sort(lambda x,y : cmp(x[0], y[0]))
    trip_list_A = []
    trip_list_B = []
    while len(tableA) > 0 and len(tableB) > 0:
        if tableA[0][0] <= tableB[0][0]: 
            dtime,atime = tableA[0]
            trip = find_longest_trip(atime, turnaround, tableB, tableA)
            trip.insert(0, (dtime, atime))
            trip_list_A.append(trip)
            for times,index in zip(trip,range(len(trip))):
                if index % 2 == 0:
                    tableA.remove(times)
                else:
                    tableB.remove(times)
        else:
            dtime,atime = tableB[0]
            trip = find_longest_trip(atime, turnaround, tableA, tableB)
            trip.insert(0, (dtime, atime))
            trip_list_B.append(trip)
            for times,index in zip(trip,range(len(trip))):
                if index % 2 == 0:
                    tableB.remove(times)
                else:
                    tableA.remove(times)
    trip_list_A.extend(tableA)
    trip_list_B.extend(tableB)
    return (len(trip_list_A),len(trip_list_B))

if __name__ == "__main__":
    input_file = file(sys.argv[1], "r")
    case_num = int(input_file.readline())
    for case in range(1, case_num + 1):
        result = analyse_case(input_file)
        print "Case #%d: %d %d" % (case, result[0], result[1])
    input_file.close()
    