#!/usr/bin/env python
import sys
import numpy

class InputException(Exception):
    pass

def parse_file(filename):
    f = file(filename, 'r')
    case_num = int(f.readline())
    lines = f.readlines()
    f.close()
    cases = []
    i = 0
    while i < len(lines):
        nums = [int(x) for x in lines[i].split()]
        i+=1
        l, t, n, c = nums[:4]
        if len(nums) - 4 != c:
            raise Exception('bah', nums)
        
        a = nums[4:]
        distances = []
        for j in xrange(n):
            distances.append(a[j % c])
        cases.append((l, t, tuple(distances)))
        
    return cases

def calculate_time(t, build_stars, distances):
    total = 0
    for i in xrange(len(distances)):
        if not build_stars[i]:
            # no booster
            total += distances[i] * 2
        else:
            if t < total:
                # already built
                total += distances[i]
            elif t < total + distances[i] * 2:
                # mid flight
                residue_build_time = t - total 
                total += residue_build_time + (distances[i] * 2 - residue_build_time) / 2.
            else:
                # not in time
                total += distances[i] * 2
    return total

CACHE = {}

def place_boosters(l, t, distances):
    if len(distances) == 0:
        return []
    if l == 0:
        return [False] * len(distances)
    
    key = (l, t, distances)
    if CACHE.has_key(key):
        return CACHE[key]
    
    no_booster = place_boosters(l, t, distances[:-1])
    CACHE[key] = no_booster + [False] 
    if l > 0:        
        with_booster = place_boosters(l - 1, t, distances[:-1])
        with_booster_time = calculate_time(t, with_booster + [True], distances) 
        no_booster_time = calculate_time(t, no_booster + [False], distances)
#        print l, distances, with_booster_time, no_booster_time
        if with_booster_time < no_booster_time:
            CACHE[key] = with_booster + [True]
        
    return CACHE[key]   

#def place_boosters(l, t, distances):        
#    n = len(distances)
#    minima = sum(distances) * 2
#    choice = [False] * n
#    if l == 2:
#        for i in xrange(n):
#            for j in xrange(i+1, n):
#                new_choice = [False] * i + [True] + [False] * (j-i-1) + [True] + [False] * (n-j-1)
#                new_time = calculate_time(t, new_choice, distances)
#                if new_time < minima:
#                    minima = new_time
#                    choice = new_choice
#    if l == 1:
#        for i in xrange(n):
#            new_choice = [False] * i + [True] + [False] * (n-i-1)
#            new_time = calculate_time(t, new_choice, distances)
#            if new_time < minima:
#                minima = new_time
#                choice = new_choice
#    return choice
            
def solve_case(l, t, distances):
    build_stars = place_boosters(l, t, distances)
    return calculate_time(t, build_stars, distances)

def main():
    global CACHE
    if len(sys.argv) != 3:
        print 'usage: %s <inputfile> <outputfile>' % sys.argv[0]
        return
    
    try:
        cases = parse_file(sys.argv[1])
    except InputException, e:
        print 'Got exception:', e
        return
    
    sys.stdout = file(sys.argv[2], 'w')
    
    for count in xrange(len(cases)):                   
        print 'Case #%d:' % (count + 1), int(solve_case(*cases[count]))
                

sys.setrecursionlimit(10000)         
if __name__=='__main__':
    main()
