#!/usr/bin/python

import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
print ' Input File',sys.argv[1]

def writetofile(line):
    filename="resA"
    fi = open(filename, "a")
    fi.write(line) # Write a string to a file
    fi.close()
#open file

f = open("A-small-attempt1.in", 'r+')
linea = f.readline()
res_number=1


List = open(sys.argv[1]).readlines()
cases=int(List[0])
List.pop(0)
#print 'Number of cases: ',cases
cases_counter=1
while cases >0:
    current_case=List[:10]
    #print List
    List.pop(0)
    #print current_case
    rowchosen1=int(current_case[0])-1
    row1=List[int(rowchosen1)]
    rowchosen2=int(current_case[5])+4
    row2=List[int(rowchosen2)]
    coincidences = 0
    my_resmynumber=-1
    print "Got ",rowchosen1," ",row1," - ",rowchosen2,row2
    #compare numbers in rows...
    for mynumber in row1.split(' '):
        #print mynumber
        for mysecondnumber in row2.split(' '):
            #print mynumber ,"is equal",mysecondnumber, "in list ", row1," & ",row2
            #print " :"+str(mynumber)+":is equal:"+str(mysecondnumber)+ ":in list ", row1," & ",row2
            if mynumber.replace('\n','') == mysecondnumber.replace('\n',''):

                coincidences=coincidences+1
                my_resmynumber = mynumber
                print "SUCCESS" +str(mynumber) + "coincendces"+str(coincidences)

    if coincidences == 1 and my_resmynumber != -1:
        writetofile("Case #"+str(cases_counter)+": "+str(my_resmynumber)+"\n")
    elif coincidences > 1 :
        writetofile("Case #"+str(cases_counter)+": Bad magician!"+"\n")
    else:
        writetofile("Case #"+str(cases_counter)+": Volunteer cheated!"+"\n")
    List.pop(0)
    List.pop(0)
    List.pop(0)
    List.pop(0)
    List.pop(0)
    List.pop(0)
    List.pop(0)
    List.pop(0)
    List.pop(0)
    cases-=1
    cases_counter+=1
