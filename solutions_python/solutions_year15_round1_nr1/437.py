#/usr/bin/env python

import sys
import numpy as np

def read_input(filename):
    f = open(filename)
    num_cases = int(f.readline())

    num_ticks = [0]*num_cases
    mushrooms = [[]]*num_cases
    for i in range(num_cases):
        num_ticks[i] = int(f.readline())
        mushrooms[i] = [0]*num_ticks[i]
        tmp_list = f.readline().split()
        for j, item in enumerate(tmp_list):
            mushrooms[i][j] = int(item)

    f.close()
    return num_ticks, mushrooms

def write_output(filename, mush_any, mush_constant):
    f = open(filename,'w')

    for i in range(len(mush_any)):
        f.write("Case #"+str(i+1)+": "+str(mush_any[i])+" "+str(mush_constant[i])+"\n")

    f.close()
    return

def count_mushrooms_eaten_any(mushrooms):
    nticks = len(mushrooms)
    mush = np.array(mushrooms)

    delta_mush = mush[:nticks-1] - mush[1:]
    
    count = 0
    #print delta_mush
    for i in range(nticks-1):
        if delta_mush[i] > 0:
            count += delta_mush[i]

    return count

def count_mushrooms_eaten_constant(mushrooms):
    nticks = len(mushrooms)
    mush = np.array(mushrooms)

    delta_mush = mush[:nticks-1] - mush[1:]

    rate = np.max(delta_mush)

    count = 0
    for i in range(nticks-1):
        if mush[i] > rate:
            count += rate
        else:
            count += mush[i]

    return count

def get_all_mushrooms_eaten(mushrooms):
    
    mush_any = [0]*len(mushrooms)
    mush_constant = [0]*len(mushrooms)
    for i in range(len(mushrooms)):
        mush_any[i] = count_mushrooms_eaten_any(mushrooms[i])
        mush_constant[i] = count_mushrooms_eaten_constant(mushrooms[i])

    return mush_any, mush_constant

if __name__ == "__main__":
    filename = sys.argv[1]

    num_ticks, mushrooms = read_input(filename)

    mush_any, mush_constant = get_all_mushrooms_eaten(mushrooms)
    
    write_output("output.txt", mush_any, mush_constant)
