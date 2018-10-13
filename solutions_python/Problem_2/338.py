#!/usr/bin/env python
'''
CodeJam 2008
Train Timetable
2008-07-17
Marc Garcia <garcia.marc@gmail.com>
'''
import sys, re

def readfile(filename):
    schedule_pattern = re.compile(r'^([0-2][0-9]):([0-5][0-9]) ([0-2][0-9]):([0-5][0-9])$')
    set_time = lambda t, d: int(t.groups()[0 + (2 * d)]) * 60 + int(t.groups()[1 + (2 * d)])
    f = open(filename, 'rb')

    data = []
    num_cases = f.readline()
    for case in xrange(int(num_cases)):
        timearound = f.readline()[:-1]
        num_dep_a, num_dep_b = f.readline()[:-1].split(' ')
        data.append([])
        for dst_num in (num_dep_a, num_dep_b):
            data[-1].append([])
            for departures in xrange(int(dst_num)):
                times = schedule_pattern.match(f.readline())
                data[-1][-1].append((set_time(times, 0), set_time(times, 1) + int(timearound)))
            data[-1][-1].sort()
    return data

def calculate(data):
    A = DEP = 0 ; B = ARR = 1

    def one_train_trips(data, current_station, next_avail):
        ''' returns schedules removing one train trips '''
        for cnt, next_req in enumerate(data[current_station]):
            if next_avail <= next_req[DEP]:
                current_trip = data[current_station].pop(cnt)
                result = one_train_trips(data, current_station ^ 1, current_trip[ARR])
                return result
        return data

    def all_train_trips(data):
        first_station = B
        if data[A] and (not data[B] or data[A][0][DEP] < data[B][0][DEP]):
            first_station = A
        current_trip = data[first_station].pop(0)
        new_data = one_train_trips(data, first_station ^ 1, current_trip[ARR])
        if data[0] or data[1]:
            result = all_train_trips(new_data)
        else:
            result = [0, 0]
        result[first_station] += 1
        return result

    for case_num, case_data in enumerate(data):
        result_from_a, result_from_b = all_train_trips(case_data)
        print 'Case #%s: %s %s' % (case_num + 1, result_from_a, result_from_b)
        
if __name__ == '__main__':
    calculate(readfile(sys.argv[1]))

