#!/usr/bin/env python
#coding=utf-8

from datetime import *

def process_timetable(str):
    tmp = str.split()
    depatrure = datetime.strptime(tmp[0], "%H:%M")
    #print depatrure
    arrival = datetime.strptime(tmp[1], "%H:%M")
    #print arrival
    
    return (depatrure, arrival)

def cmp_depature(t1, t2):    
    return cmp(t1[0], t2[0])

def cmp_arrival(t1, t2):
    return cmp(t1[1], t2[1])

def check_need_train(timetable1, timetable2, turn_around_time):
    trains = 0
    table1 = sorted(timetable1, cmp_depature)
    table2 = sorted(timetable2, cmp_arrival)
    print "sort - " ,table1
    print "sort - " ,table2
    for trip in table1:
        #print trip
        departure = trip[0]

        # looking if there is a train arrival from B
        found = False;
        for trip_2 in table2:
            arrival = trip_2[1]
            print " depatrure: ", departure,
            print " arrival: " , arrival,
            if departure - arrival >= turn_around_time :
                print " - OK"
                found = True
                table2.remove(trip_2)
                break
            else:
                print " - NO"
                
        if not found:
            trains = trains + 1
    
    if trains == 0:
        return 0
    else:
        return trains

def do_case(infile):
    turn_around_time = timedelta( minutes = int(infile.readline().strip()))
    print "turn_around_time = " , turn_around_time    
    tmp = infile.readline().strip().split()
    NA = int(tmp[0])
    NB = int(tmp[1])
    print "NA = %d, NB = %d" % (NA, NB)
    
    timetable_A = []
    for i in range(NA):
        time = infile.readline().strip()
        timetable_A.append(process_timetable(time))
    print timetable_A
    
    timetable_B = []
    for i in range(NB):
        time = infile.readline().strip()
        timetable_B.append(process_timetable(time))
    print timetable_B
    
    ####
    train_A = check_need_train(timetable_A, timetable_B, turn_around_time)
    print "need trains in A: %d" % train_A
    
    train_B = check_need_train(timetable_B, timetable_A, turn_around_time)
    print "need trains in B: %d" % train_B
    
    return (train_A, train_B)
    

def solve_question(infile, outfile, total_case):
    for i in range(total_case):
        answer = do_case(infile)
        
        str = "Case #%d: " % (i+1, ) + "%d %d" % answer
        print str
        outfile.write(str)
        outfile.write('\n')
    

def main():
    infilepath = "B-large.in"
    outfilepath = infilepath.replace(".in", ".out")
    
    ifobj = file(infilepath)
    ofobj = file(outfilepath, "w")
        
    num_of_case = int(ifobj.readline().strip())
    print int(num_of_case)
    
    solve_question(ifobj, ofobj, num_of_case)
    
    ifobj.close()
    ofobj.close()


if __name__ == "__main__":
    main()