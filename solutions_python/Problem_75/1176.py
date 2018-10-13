#!/usr/bin/env python
# encoding: utf-8
"""
Magicka.py

Created by Kelvin on 2011-05-07.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os



def main():
    case_total = int(raw_input());
    
    for case_num in range(0, case_total):
        inputs = raw_input().split(' ')
        
        combine_count = int(inputs[0])
        del inputs[0]
        combines = []
        for i in range(combine_count):
            combines.append(inputs[i])
        del inputs[0:combine_count]
        opposed_count = int(inputs[0])
        opposeds = []
        del inputs[0]
        for i in range(opposed_count):
            opposeds.append(inputs[i])
        
        del inputs[0:opposed_count]
        
        list_length = int(inputs[0])
        li = inputs[1]
        
        
        #print combines
        #print opposeds
        #print li
        
        combine_source = []
        combine_target = []
        
        for c in combines:
            combine_source.append(set([c[0], c[1]]))
            combine_target.append(c[2])
            
        opposed_set = []
        for o in opposeds:
            opposed_set.append(set([o[0], o[1]]))
        
        output = []
        
        for i in range(list_length):
            output.append(li[i])
            if 2 > len(output):
                continue
            
            last_two = set([output[-1], output[-2]])
            if last_two in combine_source:
                output[-2:] = combine_target[combine_source.index(last_two)]
            
            if 2 > len(output):
                continue
            
            for j in range(len(output) - 1):
                op_two = set([output[-1], output[j]])
                if op_two in opposed_set:
                    #del output[j:]
                    output = []
                    break
        
        print 'Case #' + str(case_num + 1) + ': [' + ', '.join(output) + ']'


if __name__ == '__main__':
    main()

