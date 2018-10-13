#!/usr/bin/env python
import sys
import array

def get_timevalue(strtime):
    l = strtime.split(":")
    value = int(l[0])*60 + int(l[1])
    return value
def get_nexttrain(t, tlist):
    for x in tlist:
        if (t['end']+turnaround_time <= x['start']) and x['is_from'] == 0:        
            return x
    return None

def sort_by_start(a,b):
    return cmp(a['start'],b['start'])

def sort_by_end(a,b):
    return cmp(a['end'],b['end'])

if __name__ == '__main__':
    num_case = int(sys.stdin.readline())    
    for ncase in range(num_case):
        turnaround_time = int(sys.stdin.readline())
        str_num_ab = sys.stdin.readline().split()
        num_a = int(str_num_ab[0])
        num_b = int(str_num_ab[1])
        
        # read NA
        na_list = []
        for x in range(num_a):
            line= sys.stdin.readline().split()
            entry = {'start':get_timevalue(line[0]), 'end':get_timevalue(line[1]), 'is_from':0 }
            na_list.append(entry)
        # read NA
        nb_list = []
        for x in range(num_b):
            line= sys.stdin.readline().split()
            entry = {'start':get_timevalue(line[0]), 'end':get_timevalue(line[1]), 'is_from':0 }
            nb_list.append(entry)        
        
        na_count = 0
        nb_count = 0
        na_list.sort(sort_by_end)
        nb_list.sort(sort_by_start)      
        for x in na_list:
            t = get_nexttrain(x,nb_list)
            if t:
                nb_count = nb_count + 1
                t['is_from'] = 1
                
        na_list.sort(sort_by_start)
        nb_list.sort(sort_by_end) 
        for x in nb_list:
            t = get_nexttrain(x,na_list)
            if t:
                na_count = na_count + 1
                t['is_from'] = 1

        print "Case #%d: %d %d"%(ncase+1, num_a-na_count, num_b-nb_count)
     

