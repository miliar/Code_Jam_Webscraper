#!/usr/bin/env pypy
import sys
import os
import argparse

PARSER = argparse.ArgumentParser()
PARSER.add_argument("input_file",
                    metavar="INPUT_FILE",
                    nargs='?',
                    type=argparse.FileType('r'),
                    default=sys.stdin)
PARSER.add_argument("output_file",
                    metavar="OUTPUT_FILE",
                    nargs='?',
                    type=argparse.FileType('w'),
                    default=sys.stdout)
ARGS = PARSER.parse_args()

def check(n):
    sn = str(n)
    for i in range(len(sn) - 1):
        if int(sn[i]) > int(sn[i+1]):
            return False
    return True

def function(n):
    if check(n):
        return int(n)
    sn = str(n)
    p = sn[0]
    lowest = int(p * len(sn))
    if lowest > int(sn):
        lowest_base = "{}{}".format(p, "0" * (len(sn) - 1))
        lowest = int(lowest_base) - 1
        sn = str(lowest)
        if check(sn):
            return int(sn)
    offset = 0
    while True:
        print("\n")
        print("sn to analyze: {}".format(sn))
        ad, d = int(sn[-2-offset]), int(sn[-1-offset])
        add = int("{}{}".format(ad, d))
        print("current two digits: {} {} = {}".format(ad, d, add))
        if int(add) == 0:
            print("arf zero")
            sn = int(sn)
            sn -= 1
            sn = str(sn)
            print("new sn because of 0: {}".format(sn))
            if check(sn):
                return int(sn)
            ad, d = int(sn[-2-offset]), int(sn[-1-offset])
            print(ad, d)
            add = int("{}{}".format(ad, d))
        if ad > d:
            print("wrong order")
            while True:
                add -= 1
                if check(add):
                    break
            add = str(add)
            if len(add) == 1:
                add = "0" + add
            print("add is good: {}".format(add))
            new_sn = sn[:-2-offset] + add
            print("partial sn: {}".format(sn))
            if offset > 0:
                print("and {}".format(sn[-offset:]))
                print(offset)
                new_sn += sn[-offset:]
            print("new sn: {}".format(new_sn))
            sn = new_sn
            if check(sn):
                return int(sn)
        offset += 1

# def function(n):
#     sn = str(n)
#     if check(sn):
#         return int(sn)
#     p = sn[0]
#     lowest = int(p * len(sn))
#     if lowest < int(sn):
#         print("ok")
#     else:
#         print("ko")

    
    

for index, l in enumerate(ARGS.input_file.readlines()[1:]):
    l = l.strip()

    N = int(l)
    result = function(N)

    ARGS.output_file.write("Case #{}: {}\n".format(index + 1, result))
