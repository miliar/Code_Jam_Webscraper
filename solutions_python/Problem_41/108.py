# Google Code Jam 2009
# Round 1B - B


# Lots of space, but helps with time
largests = {}
smallests = {}
nexts = {}
new_places = {}

def get_counts(num):
    num = str(num)
    counts = []
    for x in range(0, 10):
        counts.append(num.count(str(x)))
    return counts

def largest(counts):
    try:
        return largests[str(counts)]
    except:
        pass
    ret = ""
    for x in range(9, -1, -1):
        ret += str(x)*counts[x]
    largests[str(counts)] = ret
    return ret

def smallest(counts):
    try:
        return smallests[str(counts)]
    except:
        pass
    ret = ""
    for x in range(0, 10):
        ret += str(x)*counts[x]
    smallests[str(counts)] = ret
    return ret

def smallest_with_new_place(counts):
    try:
        return new_places[str(counts)]
    except:
        pass
    smallest_avail = 1
    while counts[smallest_avail] == 0: smallest_avail += 1
    new_count = counts[:]
    new_count[smallest_avail] -= 1
    ret = str(smallest_avail) + "0" + smallest(new_count)
    new_places[str(counts)] = ret
    return ret

def next_num(counts, num):
    """
    Returns the next largest number after num
    consisting of digit counts in 'count', plus arbitrary zeroes
    """
    try:
        return nexts[(str(counts), num)]
    except:
        pass

    if num < 10:
        return num*10
    
    if str(num) == largest(counts):
        ret = smallest_with_new_place(counts)
        nexts[(str(counts), num)] = ret
        return ret
    
    numstr = str(num)
    largest_digit = int(numstr[0])
    missing_largest = counts[:]
    missing_largest[largest_digit] -= 1
    
    same_first = next_num(missing_largest, numstr[1:])
    if len(same_first) == len(numstr)-1:
        ret = numstr[0] + same_first
        nexts[(str(counts), num)] = ret
        return ret
    else:
        if largest_digit == 9:
            print "ERROR! YOU SHOULD NOT GET HERE!"
        next_largest = largest_digit+1
        while counts[next_largest] == 0:
            next_largest += 1
        missing_next = counts[:]
        missing_next[next_largest] -= 1
        smallest_with_next = str(next_largest) + smallest(missing_next)
        ret = smallest_with_next
        nexts[(str(counts), num)] = ret
        return ret

def solve(num):
    counts = get_counts(num)
    return next_num(counts, num)

import sys
print "File?"
file = open(raw_input())
trials = int(file.readline())
for trial in range(trials):
    num = int(file.readline())
    print "Case #%s: %s" % (trial+1, solve(num))
