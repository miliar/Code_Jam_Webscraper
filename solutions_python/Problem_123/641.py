import os
import math
import sys

MAX_COUNT = 1000000000;

def get_eat_count(size, req_size):
    if size == 1:
        return (MAX_COUNT, size);
    count  = 0;
    while int(size) <= int(req_size):
        size = 2*size -1;
        count += 1;
    return(count, size + req_size)


def get_mote_count(mote_size, mote_list):
    curr_size = mote_size;
    for curr_index in xrange(0, len(mote_list)):
        ### eating_min
        if mote_list[curr_index] < curr_size:
            curr_size += mote_list[curr_index];
        else:
            if curr_index != len(mote_list)-1:
                #deleted this mote
                (add_eat_count, size) = get_eat_count(curr_size, mote_list[curr_index]);
                add_eat_count += get_mote_count(size, mote_list[curr_index+1:]);
                add_del_count = 1 + get_mote_count(curr_size, mote_list[curr_index+1:]);
                return (add_eat_count, add_del_count)[add_eat_count > add_del_count];
            else:
                return 1;
    return 0 ;

            


def prob1(input = sys.argv[1]):
    fi = open(input, "r");
    test_case_count = int(fi.readline().strip())
    for case_num in xrange(1,test_case_count+1):
        line = fi.readline();
        (mote_size, mote_count) = line.strip().split();
        line = fi.readline();
        mote_list = map(lambda x: int(x), line.strip().split());
        mote_list.sort();
        count = get_mote_count(int(mote_size), mote_list);
        print "Case #%d:  %d"%(case_num, count);


#fi = open(sys.argv[1], "r");
#for line in fi:
#    print line.strip();

prob1();
