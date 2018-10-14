import sys
finput = open(sys.argv[1], 'r')
foutput = open(sys.argv[2], 'w')

tests = finput.readline()
for test in range(int(tests)):
  line = finput.readline().split(' ')
  factorycost = float(line[0])
  addrate = float(line[1])
  goal = float(line[2])
  rate = 2.0
  timetogoal = goal / rate
  timesum = 0.0
  while True:
    timetofactory = factorycost / rate
    rate += addrate
    timesum += timetofactory
    if goal < factorycost:
      answer = timetogoal
      break
    newtime = timesum + (goal / rate)
    if newtime >= timetogoal:
      answer = timetogoal
      break
    timetogoal = goal / rate + timesum
  
  case = test  + 1
  foutput.write("Case #%s: %s" % (case, answer)) 
  foutput.write("\n")
    
  
def somefunction():
  return 0 
   