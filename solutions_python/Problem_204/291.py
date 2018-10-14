
readfile = open("B-small-attempt0.in")
writefile = open("jam_out2.txt", "w")

lines = readfile.readlines()
#assert int(lines[0]) == 100
import math
import random
      
def get_poss_vals(value,needed):
  min_val = math.ceil(value / (needed * 1.1))
  max_val = math.floor(value / (needed * 0.9))
  if min_val > max_val:
    return 0
  else:
    return min_val, max_val


flag = 0
prob_num = 0
for line_num in xrange(1,len(lines)):
  line = lines[line_num]
  if flag == 0:
    prob_num += 1
    #print "problem", prob_num 
    n, p = line.split()
    n = int(n)
    p = int(p)
    flag = 1
  elif flag == 1:
    weights = [int(x) for x in line.split()]
    #print len(weights)
    #print weights
    flag = 2
    values = []
  elif flag == 2:
    values.append([int(x) for x in line.split()])
    if len(values) == n:
      for i in xrange(n):
        bad_vals = set([])
        for x in values[i]:
          if get_poss_vals(x,weights[i]) == 0:
            bad_vals.add(x)
        good_vals = []
        for x in values[i]:
          if not x in bad_vals:
            good_vals.append(x)
        if len(good_vals) == 0:
          writefile.write("Case #%d: %d\n" % (prob_num, 0))
          flag = 0
          break
        else:
          values[i] = sorted(good_vals)
      if flag == 0:
        continue
      #print values
      #flag = 0
      score = 0
      while 1:
        max_list = []
        min_list = []
        for i in xrange(n):
          if len(values[i]) == 0:
            writefile.write("Case #%d: %d\n" % (prob_num, score))
            flag = 0
            break
        if flag == 0:
          break
        for i in xrange(n):
          #print weights[i]
          #print values[i], len(values[i])
          mn, mx = get_poss_vals(values[i][-1], weights[i])
          max_list.append(mx)
          min_list.append(mn)
        if max(min_list) <= min(max_list):
          score += 1
          for i in xrange(n):
            values[i].pop()
        else:
          #ditch the largest values
          for i in xrange(n):
            mx, mn = get_poss_vals(values[i][-1], weights[i])
            if mn > min(max_list):
              values[i].pop()
        for i in xrange(n):
          if len(values[i]) == 0:
            writefile.write("Case #%d: %d\n" % (prob_num, score))
            flag = 0
            break
        if flag == 0:
          break
