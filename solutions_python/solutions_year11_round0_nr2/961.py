#!/usr/bin/python

import sys, re

try:
    input_name = sys.argv[1]                        # Read in the supplied input file name
except IndexError:                                  # If no name was supplied:
    print 'You have not specified an input file.\n' # Return error that no input file name was supplied
    sys.exit(0)                                     # Exit
try:
    f = open(input_name,'r')                        # Try to open the file with read access
except IOError:                                     # If unable to open file:
    print "The file named '%s' does not exist, or cannot be opened.\n" % input_name # Return error that the file could not be opened
    sys.exit(0)                                     # Exit
    
l = [ re.compile("\s+").split(x) for x in [y.strip("\n") for y in f.readlines()]] 

num_trials = int(l[0][0])
rules = {}
fout = open("output.txt", "w")
def cnvstr(l):
    r = "["
    if len(l)==0:
        return "[]"
    for x in range(len(l)):
        
        if x == len(l)-1:
            r = r + l[x] + "]"
        elif x == 0:
            r = r+l[x] + ", "
        else:
            r = r + l[x] + ", "
    return r
for i in range(1,num_trials+1):
    rules[i]={"opposed":{}, "combine":{}, "result":[]}
    num_comb = int(l[i][0])
    if num_comb:
        for x in range(1,num_comb+1):
            c = l[i][x]
            rules[i]["combine"][c[:2]] = c[2]
            rules[i]["combine"][c[:2][::-1]] = c[2]
    num_opp = int(l[i][1+num_comb])
    if num_opp:
        for x in range(1,num_opp+1):
            o = l[i][1+num_comb+x]
            rules[i]["opposed"][o] = 1
            rules[i]["opposed"][o[::-1]] = 1
    rules[i]["list"] = list(l[i][len(l[i])-1])[::-1]
    while rules[i]["list"]:
        curr = rules[i]["list"].pop()
        used = False
        reset = False
        if rules[i]["result"]:
            comb = rules[i]["result"][len(rules[i]["result"])-1] + curr
            while comb in rules[i]["combine"]:
                if not used:
                    rules[i]["result"].append(curr)
                    used = True
                curr = rules[i]["combine"][comb]
                rules[i]["result"].pop()
                rules[i]["result"].pop()
                rules[i]["result"].append(curr)
                lsize = len(rules[i]["result"])
                if lsize > 1:
                    comb = rules[i]["result"][lsize-1] + rules[i]["result"][lsize-2]
                else:
                    comb = None
        if not used:
            for x in rules[i]["result"]:
                if curr+x in rules[i]["opposed"]:
                    rules[i]["result"] = []
                    reset = True
        if not reset and not used:
            rules[i]["result"].append(curr)
    fout.write("Case #" + str(i) + ": " + cnvstr(rules[i]["result"])+"\n")
fout.close()
        #######
        # for x in rules[i]["result"]:
        #     if curr+x in rules[i]["opposed"]:
        #         rules[i]["result"] = []
        #     elif:
        #         comb = rules[i]["result"][len(rules[i]["result"])-1]+x
        #         if rules[i]["result"] and comb in rules[i]["combine"]:
        #             rules[i]["result"].pop()
        #             rules[i]["result"].append(rules[i]["combine"][comb])
        #         
                
    