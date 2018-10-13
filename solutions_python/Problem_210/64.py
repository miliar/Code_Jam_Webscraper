def isc(c):
  return 1 if c=="c" else -1

def solve_rec(starting, ending, pos, deltacj, key_times_list, key_times, cache, dbg = False):
  if pos == len(key_times_list):
    if deltacj != 0:
      return None
    if starting == ending:
      return 0
    else:
      return 1
      
  time = key_times_list[pos]
  
  key = (starting, ending, pos, deltacj)
  if key in cache:
    return cache[key]
  
  if abs(deltacj) > 1440 - time:
    return None
    
  timetonext = 1440 - time if pos == len(key_times_list) - 1 else key_times_list[pos+1] - time

  if key_times[time] == "c":
    inc = (ending != "c")
    rec = solve_rec(starting, "c", pos+1, deltacj + timetonext, key_times_list, key_times, cache,dbg)
    res = None if rec is None else inc + rec
  elif key_times[time] == "j":
    inc = (ending != "j")
    rec = solve_rec(starting, "j", pos+1, deltacj - timetonext, key_times_list, key_times, cache,dbg)
    res = None if rec is None else inc + rec
  else:
    best = None
    for next in ["c","j"]:
      if next == ending:
        inc1 = (ending != next)
        rec1 = solve_rec(starting, next, pos+1, deltacj + timetonext * isc(next), key_times_list, key_times, cache,dbg)
        res1 = None if rec1 is None else inc1 + rec1
        best = minnone(res1,best)
      else:
        for i in xrange(timetonext):
          inc2 = 1
          rec2 = solve_rec(starting, next, pos+1, deltacj + i * isc(ending) + (timetonext-i) * isc(next), key_times_list, key_times, cache,dbg)
          res2 = None if rec2 is None else inc2 + rec2
          best = minnone(res2,best)
    
    res = best
    
  cache[key] = res
  return res
  
def minnone(x,y):
  if x is None:
    return y
  elif y is None:
    return x
  else:
    return min(x,y)

def solve(C,J,actC,actJ):
  
  key_times = dict()
  for c,d in actC:
    key_times[c] = "c"
    if d not in key_times:
      key_times[d] = None
  for j, k in actJ:
    key_times[j] = "j"
    if k not in key_times:
      key_times[k] = None
  
  if 0 not in key_times:
    key_times[0] = None
  
  key_times_list = list(sorted(key_times.keys()))
  
  all_times = [None] * 1440
  current = None
  for i in xrange(1440):
    if i in key_times:
      current = key_times[i]
    all_times[i] = current
  
  cache = dict()
  #for time in xrange(1440,0,-1):
  #  if time%100 == 0:
  #    print(time)
  #  for delta in xrange(-100,100):
  #    for start in ["c","j"]:
  #      for end in ["c","j"]:
  #        solve_rec(start, end,time,delta, all_times, cache)
  print(key_times_list)
  
  choice1 = solve_rec("c","c", 0, 0, key_times_list, key_times, cache, C==2)
  choice2 = solve_rec("j","j", 0, 0, key_times_list, key_times, cache, C==2)

  return minnone(choice1, choice2)

def ints(lst):
  return [int(x) for x in lst]
      
def main():
  name = "B-large"
  lines = open(name+'.in').read().split("\n")
  out = []
  num_tests = int(lines[0])
  spot = 1
  for test in xrange(num_tests):
    parts = lines[spot].split(" ")
    C = int(parts[0])
    J = int(parts[1])
    actC_raw = lines[spot+1:spot+1+C]
    actC = [ints(x.split(" ")) for x in actC_raw]
    actJ_raw = lines[spot+1+C:spot+1+C+J]
    actJ = [ints(x.split(" ")) for x in actJ_raw]
    res = "Case #%d: %d" % (test+1, solve(C,J,actC,actJ))
    out.append(res)
    print(res)
    spot += (1+C+J)

  open(name+'.out','w').write("\n".join(out))
    
main()