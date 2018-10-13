f = open("2b.txt")

for i, line in enumerate(f.readlines()[1:]):
  [C, F, X] = map(float, line.split(" "))
  
  cps = 2.0
  buy_time = 0.0
  prev_time = None

  while True:
    this_time = buy_time + (X / cps)
    if prev_time != None and this_time > prev_time:
      print("Case #%d: %f" % (i+1, prev_time))
      break
    buy_time += C / cps
    prev_time = this_time
    cps += F
