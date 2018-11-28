'''
Created on 2013/05/05

@author: hanaue51
'''

import os
import math

os.chdir("../../../data/2013/round1b/")
filename = "A-large"
postfix_in = ".in"
postfix_out = ".out"
results = []
format = "Case #%d: %s\n"

def count_operations(mote, motes):
    result = 0
    
    if len(motes) <= 0:
        return 0
    
    current_mote = mote
    motes.sort()
    
    if current_mote <= 1:
        result = len(motes)
    else:
        while len(motes) > 0:
            if current_mote > max(motes):
                break
            elif current_mote <= motes[0]:
                add_mote = current_mote
                add_count = 0
                next_mote = motes[0]
                for i in xrange(len(motes)):
                    add_mote += add_mote - 1
                    add_count += 1
                    if add_mote > next_mote:
                        add_mote += next_mote
                        break
                if add_mote <= next_mote:
                    result += len(motes)
                    break
                else:
                    res = count_operations(add_mote, motes[1:])
                    count = min(len(motes), add_count + res)
                    if count == len(motes):
                        result += count
                        break
                    else:
                        result += add_count
                        current_mote = add_mote
                        motes.pop(0)
            else:
                current_mote += motes.pop(0)
    
    return result

# read inputs
infile = open(os.getcwd() + "/" + filename + postfix_in, "r")
lines = infile.readlines()
infile.close()

cases_count = int(lines[0].strip())
for i in xrange(cases_count):
    [mote, motes_count] = [int(elem) for elem in lines[2 * i + 1].strip().split()]
    motes = [int(elem) for elem in lines[2 * i + 2].strip().split()]
    result = count_operations(mote, motes)
    results.append(format % (i + 1, result))

# write results
outfile = open(os.getcwd() + "/" + filename + postfix_out, "w")
for result in results:
#    print result
    outfile.write(result)
outfile.close()
