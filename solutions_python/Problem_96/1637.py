#!/usr/bin/env python

def calc_max(test_file):
    case_num = 1
    infile = open(test_file, 'r')
    outfile = open('Output.txt', 'a')
    for line in infile:
        if ' ' in line:
            max_count = 0
            expected_count = 0
            surprise_count = 0
            line = line.split()
            p = int(line[2])
            scores = line[3::]
            for score in scores:
                if int(score) != 0 or p == 0:
                    if 3*p-2 <= int(score):
                        expected_count += 1
                    elif 3*p-4 <= int(score):
                        surprise_count += 1
            if surprise_count > int(line[1]):
                surprise_count = int(line[1]) 
            max_count = expected_count + surprise_count
            outfile.write('Case #'+str(case_num)+': '+str(max_count)+'\n')
            case_num += 1
    infile.close()
    outfile.close()

calc_max('B-large.in')
