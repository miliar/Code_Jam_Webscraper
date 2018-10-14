#!/usr/bin/env python

import sys

def main():
  t = int(sys.stdin.readline().strip())
  line_count = 1
  for i in xrange(0,t):
    split_line = sys.stdin.readline().split()
    r = int(split_line[0])
    cur_r = 0
    cur_group = 0
    all_sum = 0
    k = int(split_line[1])
    groups = sys.stdin.readline().split()
    gis = [-1]*len(groups)
    sums = [-1]*len(groups)
    loop_done = False
    for j in xrange(0,len(groups)):
      groups[j] = int(groups[j])
    while(cur_r < r):
      if gis[cur_group] != -1 and not loop_done:
        loop_diff = cur_r - gis[cur_group]
        val_diff = all_sum - sums[cur_group]
        while( (cur_r + loop_diff) < r ):
          all_sum += val_diff
          cur_r += loop_diff
        loop_done = True
      sums[cur_group] = all_sum
      gis[cur_group] = cur_r
      cur_sum = 0
      cur_groups = 0
      while( (cur_sum + groups[cur_group]) <= k and cur_groups < len(groups)):
        cur_sum += groups[cur_group]
        cur_group = (cur_group + 1) % len(groups)
        cur_groups += 1
      all_sum += cur_sum
      cur_r += 1
    print "Case #%d: %d" % (i+1, all_sum)

if __name__ == "__main__":
  main()
