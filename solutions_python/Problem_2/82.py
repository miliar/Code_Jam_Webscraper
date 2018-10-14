import sys

class TrainSchedule:

    def __init__(self, turnaround):
        self.a_points = []
        self.b_points = []
        self.turnaround = turnaround
        
    def add_point(self, station, line):
        [s_string, e_string] = line.split(' ')
        s = string2minutes(s_string)
        e = string2minutes(e_string) + self.turnaround
        if station==1:
            self.a_points.append((s,1))
            self.b_points.append((e,-1))
        else:
            self.b_points.append((s,1))
            self.a_points.append((e,-1))

    def find_max(self):
        self.a_points.sort()
        self.b_points.sort()
        a_max = 0
        a_current = 0
        b_max = 0
        b_current = 0
        for point in self.a_points:
            a_current += point[1]
            if a_current>a_max:
                a_max = a_current
        for point in self.b_points:
            b_current += point[1]
            if b_current>b_max:
                b_max = b_current
        return [a_max, b_max]


def processFile(source, target):
    sf = open(source)
    tf = open(target,"w")
    num_cases = int(sf.readline())
    for case in range(1,num_cases+1):
        turnaround = int(sf.readline())
        train_schedule = TrainSchedule(turnaround)
        num_points = sf.readline().split(' ')
        [num_a, num_b] = [int(e) for e in num_points]
        for i in range(0,num_a):
            train_schedule.add_point(1,sf.readline().strip('\n'))
        for i in range(0,num_b):
            train_schedule.add_point(2,sf.readline().strip('\n'))
        [result_a, result_b] = train_schedule.find_max()
        newline = 'Case #' + repr(case) + ': ' + repr(result_a) + ' ' + repr(result_b)
        #print(newline)
        tf.write(newline)
        if not case==num_cases: tf.write('\n')

    sf.close
    tf.close
    
def string2minutes(string):
    [h,d] = string.split(':')
    return int(h)*60 + int(d)

def main(argv = None):
    if argv is None:
        argv = sys.argv
    if (len(argv)>2):
        processFile(argv[1], argv[2])
    
if __name__ == "__main__":
    main()