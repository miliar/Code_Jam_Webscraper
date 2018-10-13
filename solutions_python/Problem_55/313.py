import sys
import os

def ridespecs(peoplelist, ridesize, pos_count):
    peoplecount = 0
    peopleno = len(peoplelist)
    if pos_count >= peopleno:
       pos_count = 0
    # print "----------------"
    #print "Start Pos: %d"%(pos_count)
    #print ridesize , pos_count
    while ridesize > peoplecount:
        peoplecount = peoplecount + peoplelist[pos_count]
        #print "COUNTER FLOW : %d -------- %d"%(peoplecount, pos_count)
        pos_count = pos_count + 1
        if pos_count >= peopleno:
            pos_count = 0
   # print "@@@@@@@@ RIDE SIZE:%d PEOPLE COUNT:%d"%(ridesize, peoplecount)
    pos_count = (pos_count+peopleno - 1)%(peopleno)
    if ridesize != peoplecount:
        #print "reducing value"
        peoplecount = peoplecount - peoplelist[pos_count] 
        pos_count = (pos_count+peopleno - 1)%(peopleno)
    #print "End Pos:%d \nPeople count%d"%(pos_count, peoplecount)
    return peoplecount, pos_count 

    

def sale_counter(peoplelist, ridecount, ridesize):
    pos_count = 0
    ridecounter = 1
    total_sale = 0
    people_no = reduce(lambda x,y : x+y , peoplelist)
    if people_no <= ridesize:
        return (people_no*ridecount)
    while (ridecount >= ridecounter):
        cost, pos_count = ridespecs(peoplelist, ridesize, pos_count)
        #print cost, pos_count
        pos_count=pos_count + 1
        ridecounter = ridecounter + 1
        total_sale = total_sale + cost
    return total_sale

def roller_coaster(filename, outputfile):
    lines = open(filename,'r').readlines()
    outputdata = ""
    testcase_count = int(lines[0])
    counter=1
    linecounter = 1
    #print "here"
    for line in lines[1:]:
        try:
	    if(linecounter%2 == 1 ):
                ridecount, ridesize, people_waste_count = map(int, line.split())
            else :
                peoplelist = map(int, line.split())
               # print peoplelist
                totalsale = sale_counter(peoplelist, ridecount, ridesize)
                #print "+_________________________"
                outputdata = outputdata  + "Case #%d: %s\n"%(counter, totalsale)
                counter = counter + 1
        except Exception as e:
            print e
            counter = counter + 1
            continue
        linecounter = linecounter + 1
    outputdata = outputdata.strip()
    open(outputfile, 'w').write(outputdata)
    #print outputdata

if __name__=="__main__":
    try:
        roller_coaster(sys.argv[1], sys.argv[2])
    except Exception as e:
        print "Error cause :%s"%e

