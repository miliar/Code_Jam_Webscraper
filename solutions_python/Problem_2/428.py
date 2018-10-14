#set dubug to off
DEBUG = -1

import sys

def DepartStationAtTime(ReadyTrains,Time):
##    print "Departing at:",Time
##    print "Trains Ready to leave at:",ReadyTrains
    for item in ReadyTrains:
        if item <= Time:
            return item
    
    return ""

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print "Usage: TrainTime.py <input file>"
        print "Trying to load default files"
        try:
            input_file = open('C:\B-small-attempt0.in')
            output_file = open('B-small-output.txt','w')
        except:
            print "couldn't load default filename, see usage"
            exit()
    else:
        try:
            #we asume that the first arg is the input file name
            input_file = open(sys.argv[1])
            output_file = open('B-small-output.txt','w')
        except:
            print "Usage: TrainTime.py <input file>"
            print "couldn't open the specified file name"
            exit()
    

    count = int(input_file.readline()[:-1])
    
    for x in range(count):
        output_file.write("Case #" + str(x+1) +": ")

        if x == DEBUG:
            print "Time Table #",x+1
        
        turnaround = int(input_file.readline()[:-1])
        NaNb_list = input_file.readline()[:-1].split(" ")
        NA = int(NaNb_list[0])
        NB = int(NaNb_list[1])

        if x == DEBUG:
            print "Turnaround Time:",turnaround
            print "Trips from A to B:",NA
            print "Trips from B to A:",NB

        TrainStartingCountA = 0
        TrainStartingCountB = 0

        DeparturesFromA = []
        ArrivalsFromA = []
        DeparturesFromB = []
        ArrivalsFromB = []
        
        AReadyTrains = []
        BReadyTrains = []

        for y in range(NA):
            NA_time_list = input_file.readline()[:-1].split(" ")
            DeparturesFromA.append(int(NA_time_list[0].replace(":","")))
            ArrivalsFromA.append(int(NA_time_list[1].replace(":","")))
            
        for y in range(NB):
            NB_time_list = input_file.readline()[:-1].split(" ")
            DeparturesFromB.append(int(NB_time_list[0].replace(":","")))
            ArrivalsFromB.append(int(NB_time_list[1].replace(":","")))

        if x == DEBUG:
            print "Departures from A:",DeparturesFromA
            print "Departures from B:",DeparturesFromB
            print "Arrivals from A:",ArrivalsFromA
            print "Arrivals from B:",ArrivalsFromB

        for item in ArrivalsFromB:
            AReadyTrains.append(item+turnaround)        

        for item in ArrivalsFromA:
            BReadyTrains.append(item+turnaround)


        DeparturesFromA.sort()
        ArrivalsFromA.sort()
        DeparturesFromB.sort()
        ArrivalsFromB.sort()
        AReadyTrains.sort()
        BReadyTrains.sort()

        if x == DEBUG:
            print "Trains Ready to leave A at:",AReadyTrains
            print "Trains Ready to leave B at:",BReadyTrains

        for item in DeparturesFromA:
            if (DepartStationAtTime(AReadyTrains,item)):
                if x == DEBUG:
                    print "A train was ready to depart A"
                AReadyTrains.remove(DepartStationAtTime(AReadyTrains,item))
            else:
                if x == DEBUG:
                    print "You need another train at A"
                TrainStartingCountA += 1

        for item in DeparturesFromB:
            if (DepartStationAtTime(BReadyTrains,item)):
                if x == DEBUG:                
                    print "A train was ready to depart B"
                BReadyTrains.remove(DepartStationAtTime(BReadyTrains,item))
            else:
                if x == DEBUG:
                    print "You need another train at B"
                TrainStartingCountB += 1
                
        if x == DEBUG:
            print "Trains needed at A:",TrainStartingCountA
            print "Trains needed at B:",TrainStartingCountB
            print TrainStartingCountA,TrainStartingCountB

        output_file.write(str(TrainStartingCountA) + " " + str(TrainStartingCountB)+"\n")

    print "output went to:",output_file.name
    
    output_file.close()
    input_file.close()
    

    
