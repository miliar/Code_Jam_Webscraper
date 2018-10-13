DEBUG = 1

def log(msg):
  if DEBUG:
    print msg

for caseno in range(int(raw_input())):
  rt = int(raw_input())
  a, b = map(int, raw_input().split())
  a_start = []
  a_stop = []
  b_start = []
  b_stop = []
  tt_dict = {}
  for ign in range(a):
    start, stop = raw_input().split()
    time = int(start.split(":")[0]) * 60 + int(start.split(":")[1])
    events = tt_dict.get(time, [])
    events.append("a_start")
    tt_dict[time] = events
    time = int(stop.split(":")[0]) * 60 + int(stop.split(":")[1]) + rt
    events = tt_dict.get(time, [])
    events.append("a_stop")
    tt_dict[time] = events
  for ign in range(b):
    start, stop = raw_input().split()
    time = int(start.split(":")[0]) * 60 + int(start.split(":")[1])
    events = tt_dict.get(time, [])
    events.append("b_start")
    tt_dict[time] = events
    time = int(stop.split(":")[0]) * 60 + int(stop.split(":")[1]) + rt
    events = tt_dict.get(time, [])
    events.append("b_stop")
    tt_dict[time] = events
  tt = tt_dict.keys()
  tt.sort()
  a_avail = 0
  b_avail = 0
  a_needed = 0
  b_needed = 0
  for time in tt:
    events = tt_dict[time]
    a_avail += reduce(lambda a, b: a + 1, [x for x in events if x == "b_stop"], 0)
    b_avail += reduce(lambda a, b: a + 1, [x for x in events if x == "a_stop"], 0)
    a_avail -= reduce(lambda a, b: a + 1, [x for x in events if x == "a_start"], 0)
    b_avail -= reduce(lambda a, b: a + 1, [x for x in events if x == "b_start"], 0)
    if a_avail < 0:
      a_needed += abs(a_avail)
      a_avail = 0
    if b_avail < 0:
      b_needed += abs(b_avail)
      b_avail = 0

  print "Case #%s: %s %s" % (str(caseno + 1), str(a_needed), str(b_needed))