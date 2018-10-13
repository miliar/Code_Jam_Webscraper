#!/usr/bin/env python

def omit_colon(s):
    ss = s[0].split(':')
    s[0] = int(ss[0])*60 + int(ss[1])
    ss = s[1].split(':')
    s[1] = int(ss[0])*60 + int(ss[1])
    return s



testcases = int(raw_input())
t = 1
while t <= testcases:
    turn_around_time = int(raw_input())
    str = raw_input()
    str = str.split()
    NA = int(str[0])
    NB = int(str[1])
    
    timetableA = []
    timetableB = []
    i = 0
    while i < NA:
        start_stop = raw_input()
        start_stop = start_stop.split()
        omit_colon(start_stop)
        timetableA.append(start_stop)
        i += 1
    
    i = 0
    while i < NB:
        start_stop = raw_input()
        start_stop = start_stop.split()
        omit_colon(start_stop)
        timetableB.append(start_stop)
        i += 1
        
    timetableA.sort()
    timetableB.sort()
    
    #print timetableA
    #print timetableB
    #
    i = j = 0
    train_waiting_atA = []
    train_waiting_atB = []
    train_starting_from_A = train_starting_from_B = 0
    
    while True:
        #print "i: %d \t j: %d" % (i, j)
        
        if i<NA and j<NB and timetableA[i][0] <= timetableB[j][0]:
            if len(train_waiting_atA) > 0 and train_waiting_atA[0] <= timetableA[i][0]: del(train_waiting_atA[0])
            else: train_starting_from_A += 1
            train_waiting_atB.append(timetableA[i][1] + turn_around_time)
            train_waiting_atB.sort()
            i += 1
            
        elif i<NA and j<NB and timetableA[i][0] > timetableB[j][0]:
            if len(train_waiting_atB) > 0 and train_waiting_atB[0] <= timetableB[j][0]: del(train_waiting_atB[0])
            else: train_starting_from_B += 1
            train_waiting_atA.append(timetableB[j][1] + turn_around_time)
            train_waiting_atA.sort()
            j += 1
            
        elif i<NA:
            if len(train_waiting_atA) > 0 and train_waiting_atA[0] <= timetableA[i][0]: del(train_waiting_atA[0])
            else: train_starting_from_A += 1
            i += 1
    
        elif j<NB:
            if len(train_waiting_atB) > 0 and train_waiting_atB[0] <= timetableB[j][0]: del(train_waiting_atB[0])
            else: train_starting_from_B += 1
            j += 1
        else:
            break
        
    print "Case #%d: %d %d" % (t, train_starting_from_A, train_starting_from_B)
            
    t += 1

    