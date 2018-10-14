#!/usr/bin/env python

from __future__ import print_function
import sys

import math


def def_nonbase(list):
    nonbase = {}
    for newelem in list:
        nonbase[newelem[0]+newelem[1]] = newelem[2]
        nonbase[newelem[1]+newelem[0]] = newelem[2]
    return nonbase

def invoke_elem(invoke, nonbase_dict, oppose):
    elem_list= []
    for elem in invoke:
        elem_list.append(elem)
        # print(str(elem_list[-2:]))
        if(len(elem_list) >= 2):
            if(nonbase_dict.has_key(elem_list[-2]+elem_list[-1])):
                # print("detected reaction")
                elem_list[-2:] = nonbase_dict[elem_list[-2]+elem_list[-1]]
            else:
                for opp in oppose:
                    if((opp[0] in elem_list) and (opp[1] in elem_list)):
                        elem_list = []
    return elem_list

def output_elem_list(case_num, elem_list, output_file):
    print("Case #%d: [" % (case_num), end="", file=output_file)
    if(len(elem_list) > 0):
        print(elem_list[0], end="", file=output_file)
        for elem in elem_list[1:]:
            print(",",elem, end="", file=output_file)
    print("]", file=output_file)

def main(*args):
    if(len(args) < 2):
        print("Usage: %s <input file>" % args[0])

    filename = args[1]
    input_file = open(filename, "rb")
    output_file = open(filename+".out", "wb")

    try:
        input = input_file.readline().strip()
    except:
        print("Premature end of input")

    T = int(input)
    for i in range(T):
        try:
            inputs = input_file.readline().split()
        except:
            print("Premature end of input")

        nonbase = []
        oppose = []
        invoke = ""

        j = 0
        C = int(inputs[j])
        for k in range(C):
            j = j + 1
            nonbase.append(inputs[j])

        j = j + 1
        D = int(inputs[j])
        for k in range(D):
            j=j+1
            oppose.append(inputs[j])

        j = j + 1
        N = int(inputs[j])
        invoke = inputs[j+1]

        # print(nonbase, oppose, invoke)
        nonbase_dict = def_nonbase(nonbase)
        # print(nonbase_dict, oppose)

        elem_list = invoke_elem(invoke, nonbase_dict, oppose)
        output_elem_list(i+1, elem_list, output_file)

    input_file.close()
    output_file.close()


if(__name__ == "__main__"):
    sys.exit(main(*sys.argv))
