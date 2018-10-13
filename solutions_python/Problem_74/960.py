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
bots = {"O":{}, "B":{}}
other = {"O":"B", "B":"O"}
exec_list = {}
results = {}
for i in range(1,num_trials+1):
    exec_list[i]=[]
    results[i] = 0
    for b in bots:
        bots[b][i]={"list":[], "curr_pos":1}
    num_presses = int(l[i][0])
    # print l[i] print each trial
    for j in range(num_presses):
        pair = bot, button = l[i][j*2+1], int(l[i][j*2+2])
        exec_list[i].append(pair)
        bots[bot][i]["list"]= bots[bot][i]["list"] + [button]
    for b in bots:
        bots[b][i]["list"].reverse()

#################################################
#                 Print bots                    #
#################################################
# for b in bots:                                #
#     print "%s" % b                            #
#     for t in bots[b]:                         #
#         print "\t%s" % t                      #
#         for x in bots[b][t]:                  #
#             print "\t\t%s" % bots[b][t][x]    #
#################################################
fout = open("output.txt", "w")
for i in range(1, num_trials+1):
    exec_list[i].reverse()
    while exec_list[i]:
        b, pos = exec_list[i].pop() # curr == ["BOT", ##to go to]
        curr_cost = abs(pos - bots[b][i]["curr_pos"]) + 1 # 1 is cost to press button
        bots[b][i]["curr_pos"] = pos
        results[i] = results[i] + curr_cost
        assert(bots[b][i]["list"].pop() == bots[b][i]["curr_pos"] == pos)
        ## update other bot
        oth = other[b]
        if bots[oth][i]["list"]:
            dest = bots[oth][i]["list"][ len(bots[oth][i]["list"]) - 1 ]
            cp = bots[oth][i]["curr_pos"]
            diff = dest - cp
            if curr_cost >= abs(diff):
                bots[oth][i]["curr_pos"] = dest
            else:
                bots[oth][i]["curr_pos"] = cp + curr_cost * (diff/ abs(diff))
    fout.write( "Case #" + str(i) + ": "+ str(results[i])+"\n")
fout.close()
        
    
    