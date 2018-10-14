#encoding:utf-8
import sys

def read():
    cases = 0
    sets = []
    num = 1
    for line in sys.stdin:
        line = line.strip()
        if not cases: 
            cases = int(line)
            continue
        row = num % 10    
        if row == 1 and sets:
            yield sets
            sets = []
        nums = [int(n) for n in line.split()]
        sets.append(nums if len(nums) > 1 else nums[0]) 
        num += 1
    else: 
        if sets: yield sets

mcases = 1
for sets in read():
    mix = set(sets[sets[0]]) & set(sets[sets[5] + 5])
    if not mix:
        print "Case #%d: Volunteer cheated!" % mcases
    else:
        print "Case #%d: %s" % (mcases, list(mix)[0]) if len(mix) == 1 else "Case #%d: Bad magician!" % mcases
    mcases += 1        

        



