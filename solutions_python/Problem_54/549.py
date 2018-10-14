import sys
import os
import operator

def gcd (numA, numB):
    while numB != 0:
        numRem = numA % numB
        numA = numB
        numB = numRem
    return numA

def new_warning_date(event_list):
    #event_list.sort(reverse=True)
    eventmap = []
    for counter in range(1, len(event_list)):
        eventmap.append(operator.abs(event_list[counter] - event_list[counter-1]))
    #print eventmap
    if len(eventmap) == 1:
       max_gcd = eventmap[0]
    else:
       max_gcd = reduce(lambda x,y: gcd(x,y), eventmap)
    #print max_gcd
    term = min(event_list)
    if term <= max_gcd:
       additive = max_gcd - term
    elif term%max_gcd == 0:
       additive = term % max_gcd
    else:
       additive = (max_gcd - (term % max_gcd))
    return additive

def warning(filename, outputfile):
    lines = open(filename,'r').readlines()
    outputdata = ""
    testcase_count = int(lines[0])
    counter=1
    for line in lines[1:]:
        data = map(int,line.split())
        event_list = data[1:]
        #print event_list
        date  = new_warning_date(event_list)
        outputdata = outputdata  + "Case #%d: %s\n"%(counter, date)
        counter = counter + 1
    outputdata = outputdata.strip()
    open(outputfile, 'w').write(outputdata)
    #print outputdata

if __name__=="__main__":    
    warning(sys.argv[1], sys.argv[2])


