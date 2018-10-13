#!/usr/bin/env python
#-*- coding:utf-8 -*-

def add(time, mn):
    hours, minutes = map(int, time.split(":"))
    if minutes + mn >= 60:
        hours = hours + 1
    minutes = (minutes + mn) % 60
    return "%02d:%02d" % (hours, minutes)

def numbers(timetable):
    """
    1 : depart from A
    2 : depart from B
    -1 : ready in A
    -2 : ready in B
    """
    
    A = B = 0
    in_A = in_B = 0
    
    for time, values in timetable:
        for value in values:
            if value == 1:
                if in_A == 0:
                    A += 1
                else:
                    in_A -= 1
            
            elif value == 2:
                if in_B == 0:
                    B += 1
                else:
                    in_B -= 1
            
            elif value == -1:
                in_A += 1
            elif value == -2:
                in_B += 1

    return A, B

def test():
    pass

if __name__ == '__main__':
    from sys import argv, exit
    if len(argv) < 2:
        test()
        exit()
    
    file_name = argv[1]
    lines = open(file_name).read().split('\n')[0:-1]
    nb_inputs = int(lines[0])
    line_no = 0
    lines = lines[1:]
    
    for n in range(nb_inputs):
        turnaround = int(lines[line_no])
        NA, NB = map(int, lines[line_no+1].split(" "))
        line_no += 2
        from_A = []
        to_A = []
        from_B = []
        to_B = []
        for i in range(NA):
            line = lines[line_no + i]
            time_from_A, time_to_B = line.split(" ")
            from_A.append(time_from_A)
            to_B.append(add(time_to_B, turnaround))
        for i in range(NA, NA + NB):
            line = lines[line_no + i]
            time_from_B, time_to_A = line.split(" ")
            from_B.append(time_from_B)
            to_A.append(add(time_to_A,turnaround))
        
        line_no += NA + NB
        timetable = {}
        
        for time in from_A:
            if time not in timetable:
                timetable[time] = []
            timetable[time].append(1)
        for time in to_A:
            if time not in timetable:
                timetable[time] = []
            timetable[time].append(-1)
        for time in from_B:
            if time not in timetable:
                timetable[time] = []
            timetable[time].append(2)
        for time in to_B:
            if time not in timetable:
                timetable[time] = []
            timetable[time].append(-2)
        
        for value in timetable.values():
            value.sort()
        
        timetable = timetable.items()
        timetable.sort()
        #from pprint import pprint
        #pprint(timetable)
        A, B = numbers(timetable)
        print 'Case #%s:' % (n+1), A, B

