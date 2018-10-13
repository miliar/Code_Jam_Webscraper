def get_tidy(num):
  inflection_index = 0
  inflection_val = int(num[0])
  # search from front to back until we find the value which is greater than the value after
  for i in xrange(len(num)-1):
    val = int(num[i])
    if val != inflection_val:
      inflection_index, inflection_val = i, val
    next_val = int(num[i+1])
    # found a value greater than next val, so return a string for which
    # val is decremented (and all preceding same as val) and everything after = 9 
    if val > next_val:
      s = ''
      # convert parts until to inflection_index
      for j in xrange(inflection_index+1):
        traceback_val = int(num[inflection_index-j])
        if traceback_val == val:
          if val != 1: s = s + str(traceback_val-1)
        else:
          # not same as val, everything up to here (index inflection_index-j) remains the same as before
          for k in xrange(inflection_index-j+1):
            s = num[k] + s
          break
      # convert parts after inflection_index
      s += '9' * (len(num)-inflection_index-1)
      return s
  # the number was already tidy
  return num

with open('B-small-attempt0.in', 'r') as f:
  with open('b.out', 'w') as out:
    lines = [ x.strip() for x in f.readlines() ]
    T = int(lines[0])
    for i in xrange(T):
      num = lines[i+1]
      tidy = get_tidy(num)
      out.write('Case #%d: %s\n' % (i+1, tidy))