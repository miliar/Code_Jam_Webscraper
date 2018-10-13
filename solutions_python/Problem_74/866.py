# Copyright (c) 2011 Jann Kleen jann@pocketvillage.com
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

# from https://github.com/JannKleen/CodeJamHelper
from codejamio import *
from codejamhelper import *


from itertools import izip

# helpers
def zip_chunkwise(t, size=2):
    it = iter(t)
    return izip(*[it]*size)
    
def transposed(lists):
    if not lists: return []
    return map(lambda *row: list(row), *lists)
    
def turn_90_cw(lists):
    lists = transposed(lists)
    for li in lists:
        li.reverse()
    return lists
    
def turn_90_ccw(lists):
    lists = transposet(lists)
    lists.reverse()
    return lists
    
# data types
list_of_ints = lambda x: map(int, x.split())

# Qualification - A
cases = CodeJamHelper(get_file()).getInputList()
results = []
def get_next(bot, steps):
    try:
        targ =  filter(lambda x: x[0] == bot, steps)[0][1]
        return int(targ)
    except IndexError:
        return None

for case in cases:
    case = case.split()[1:]
    steps = list(zip_chunkwise(case))
    count = 0
    obot = 1
    bbot = 1
    odest = get_next('O', steps) 
    bdest = get_next('B', steps)
    wfor = steps.pop(0)
    while True:
        if obot == odest:
            # obot reached target
            odest = -1
        elif wfor and wfor[0] == 'O' and odest == -1:
            wfor = None
            nxt = get_next('O', steps)
            if nxt:
                # set next target
                if nxt == obot:
                    odest = -1
                else:
                    odest = nxt
        if odest < obot and odest != -1:
            obot -= 1
        elif odest > obot and odest != -1:
            obot += 1

        if bbot == bdest:
            # bbot reached target
            bdest = -1
        elif wfor and wfor[0] == 'B' and bdest == -1:
            nxt = get_next('B', steps)
            wfor = None
            if nxt:
                # set next target
                if nxt == bbot:
                    bdest = -1
                else:
                    bdest = nxt
        if bdest < bbot and bdest != -1:
            bbot -= 1
        elif bdest > bbot and bdest != -1:
            bbot += 1
        if steps:
            if wfor == None:
                wfor = steps.pop(0)
            #print steps
        elif wfor == None:
            results.append(count)
            break
        count += 1
        print "obot:%s odest:%s bbot:%s bdest:%s wfor:%s step:%s" % (obot, odest, bbot, bdest, wfor, count)    

put_file(results)