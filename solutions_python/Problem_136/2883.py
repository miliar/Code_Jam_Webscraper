import sys

def solve_case(C, F, X):
  start_time = 0.0
  production_rate = 2.0

  while True:
    time_to_finish_at_current_rate = X / production_rate
    time_to_farm = C / production_rate
    
    time_left_at_current_rate_after_farm = time_to_finish_at_current_rate - time_to_farm
    time_to_finish_with_another_farm = X / (production_rate + F)
    
    if time_left_at_current_rate_after_farm > time_to_finish_with_another_farm:
      start_time = start_time + time_to_farm
      production_rate = production_rate + F
    else:
      return start_time + time_to_finish_at_current_rate

filename = sys.argv[1]

infile = open(filename)

T = int(infile.readline())

for x in range(T):
  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  sys.stdout.write(": ")
  
  line = [float(v) for v in infile.readline().split()]
  C = line[0]
  F = line[1]
  X = line[2]
  
  print str(round(solve_case(C, F, X), 7))
  
infile.close()