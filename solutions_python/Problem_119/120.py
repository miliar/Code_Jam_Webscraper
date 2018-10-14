#!/usr/bin/env python

import sys
from collections import defaultdict

def main():
    count = int(sys.stdin.readline())
    for case in xrange(1,count+1):
        sys.stderr.write("case %d\n" % case)
        info = Info()
        if (not info.possible()):
            print "Case #%d:" % case, "IMPOSSIBLE"
            continue
        out = try_solve(info.initkeys, list(), info)
        if(out):
            print "Case #%d:" % case, str.join(" ", map(str,out))
        else:
            print "Case #%d:" % case, 'IMPOSSIBLE'
        sys.stderr.write("done\n")

class Info:
    def __init__(self):
        line = sys.stdin.readline().rstrip()
        nbox = int(line.split()[1])
        keys = defaultdict(lambda:0)
        line= sys.stdin.readline().rstrip()
        for key in line.split(): keys[int(key)] += 1
        contain = defaultdict(lambda:[])
        open_by = defaultdict(lambda:[])
        key_of = dict()
        key_offer = dict()
        for box in xrange(1, nbox+1):
            nums = [int(i) for i in sys.stdin.readline().rstrip().split()]
            key_of[box] = nums[0]
            open_by[nums[0]].append(box)
            contain[box] = nums[2::]
            key_offer[box] = set(contain[box]).difference([key_of[box]])
        (self.nbox, self.initkeys) = (nbox, keys)
        (self.contain, self.open_by, self.key_of) = (contain, open_by, key_of)
        self.key_offer = key_offer
        
    def possible(self):
        key_count = defaultdict(lambda:0, self.initkeys.copy())
        for keys in self.contain.values():
            for key in keys:
                key_count[key]+=1
        keys = set(self.key_of.values())
        key_needed = dict([(key, self.key_of.values().count(key)) for key in keys])
        for key in keys:
            if (key_needed[key] > key_count[key]):
                return False
        return True

def check_keytype(keys, opened, info):
    unopened = list(set(range(1,info.nbox+1)).difference(opened))
    keytype_offer = reduce(lambda x,y: x.union(y), 
            [info.key_offer[box] for box in unopened],
            set(filter(lambda k: keys[k] > 0, keys.keys())))
    keytype_needed = set([info.key_of[box] for box in unopened])
    extra = keytype_needed.difference(keytype_offer)
    return not extra
    

def openbox(box, keys, opened, info):
    keys[info.key_of[box]] -=1
    for key in info.contain[box]: keys[key] +=1
    opened.append(box)
    return (keys, opened, info)

def backtrace(opened, keys, info):
    box = opened.pop()
    keys[info.key_of[box]] +=1
    for key in info.contain[box]: keys[key] -=1
    

def avialable(keys, opened, info):
    avi_keys = filter(lambda k: keys[k] > 0, keys)
    can_open = reduce(lambda x,y: x.union(y), [info.open_by[key] for key in avi_keys], set())
    can_open.difference_update(opened)
    can_open = sorted(list(can_open))
    return can_open

def try_solve(keys, opened, info):
    if(len(opened) == info.nbox): 
        return opened
    can_open = avialable(keys, opened, info)
    if(len(can_open) == 0): 
        return False
    for box in can_open:
        openbox(box,keys,opened,info)
        if(check_keytype(keys,opened,info) == False):
            backtrace(opened,keys,info)
            continue
        solved = try_solve(keys, opened, info)
        if(solved): 
            return solved
        else:
            backtrace(opened, keys, info) 

    return False

main()

