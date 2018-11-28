#! /usr/bin/env python

import time

start_time = time.time()

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def check(node1, node2):
    if node1['mini'] > node2['mini']:
        return False
    elif node1['mini'] < node2['mini']:
        return True
    else:
        if node1['maxi'] > node2['maxi']:
            return False
        elif node1['maxi'] < node2['maxi']:
            return True
        else:
            if node1['i'] < node2['i']:
                return False
            elif node1['i'] > node2['i']:
                return True

def sort(combs, new_combinations):
    for i, e in enumerate(new_combinations):
        l = len(combs)
        if l:
            f = True
            while f:
                l = l- 1
                if check(e, combs[l]):
                    combs = combs[:l+1] + [e] + combs[l+1:]
                    f = False
                elif l == 0:
                    combs = combs[:l] + [e] + combs[l:]
                    f = False
        else:
            combs = [e]
    return combs

def split_or_calculate(li, ri):
    diff = ri-li

    if diff % 2 is 0:
        i = (ri+li)/2
    else:
        i = int((ri+li)/2)
    mini = i - li
    maxi = ri - i
    return dict(i=i, mini=mini, maxi=maxi, li=li, ri=ri)

def main (n, k):
    combinations = [{'ri': n-1, 'li': 0}]
    latest_node = {}
    for c in range(1, k+1):
        ri = combinations[0]['ri']
        li = combinations[0]['li']
        latest_node = split_or_calculate(li, ri)
        left_combination = split_or_calculate(latest_node['li'], latest_node['i']-1)
        right_combination = split_or_calculate(latest_node['i']+1, latest_node['ri'])
        combinations = sort(combinations[1:], [left_combination, right_combination])


    return latest_node['maxi'], latest_node['mini']


if __name__ == "__main__":
    t = int(raw_input().strip()) # read a line with a single integer
    for i in xrange(1, t+1):
      n, k = [int(s) for s in raw_input().split(' ')] # read a list of integers, 2 in this case
      y, z = main(n, k)
      print "Case #{}: {} {}".format(i, y, z)
    # print("--- %s seconds ---" % (time.time() - start_time))
