#!/usr/bin/env pypy
import sys, os

def solving(case, c, f, x):
    current_rate = 2
    build_time = 0
    old_time = x / current_rate
    new_time = old_time
    while old_time >= new_time:
        old_time = new_time
        build_time += c / current_rate
        current_rate += f
        new_time = build_time + x / current_rate
    result =  "%.7f" % old_time
    outfile.write("Case #%d: %s\n" % (case, result))

outfile = open("%s.out" % sys.argv[1], "w")
with open(sys.argv[1]) as infile:
    for case, values in enumerate(infile.readlines()[1:]):
        solving(case + 1, *map(float, values.split()))
        
outfile.close()
