#!/usr/bin/python2.5

N = input()
needle = "welcome to code jam"

idx = 0
needle_positions = {}
for c in needle: 
    if not (c in needle_positions): needle_positions[c] = []
    needle_positions[c].append(idx)
    idx = idx+1
for c in needle: needle_positions[c] = sorted(needle_positions[c])

for case in range(N):
    haystack = raw_input()
    prefix_count = []
    for j in range(19): prefix_count.append(0)
    for c in haystack:
        if (c in needle_positions):
            for possible_pos in needle_positions[c]:
                if (possible_pos == 0):
                    prefix_count[possible_pos] += 1
                else:
                    prefix_count[possible_pos] += prefix_count[possible_pos-1]
                if (prefix_count[possible_pos] > 10000): prefix_count[possible_pos] -= 10000
    answer = "0000"+str(prefix_count[18])
    print "Case #%d: %s" % (case+1, answer[-4:])
