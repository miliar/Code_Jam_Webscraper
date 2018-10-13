import sys

def process_test_case(infile):
  params = infile.readline().split()
  R = int(params[0])
  k = int(params[1])
  N = int(params[2])
  
  groups = infile.readline().split()
  groups_as_int = []
  for j in groups:
    groups_as_int.append(int(j))
  
  total_euros_on_ride_r = {}
  total_euros_on_ride_r[0] = 0
  cursor = 0;
  keep_going = 1;
  r = 0;
  cycle_length = 0
  
  while r < R and keep_going == 1:
    r += 1
    filled_seats = 0
    fill_seats = 1
    old_cursor = cursor    
    
    while fill_seats == 1:
      gi = groups_as_int[cursor]
      
      if (gi <= k - filled_seats):
        filled_seats += gi
        cursor += 1
        
        if (cursor >= N):
          cursor -= N
          if cursor == old_cursor:
            keep_going = 0
            cycle_length = r
            fill_seats = 0
          
      else:
        fill_seats = 0
        if (cursor == 0):
          keep_going = 0
          cycle_length = r
          
    total_euros_on_ride_r[r] = total_euros_on_ride_r[r-1] + filled_seats

  full_cycles = 0
  remaining_runs = r
  
  if (cycle_length > 0):
    full_cycles = int(R // cycle_length)
    remaining_runs = R - (cycle_length * full_cycles)

  total_euros = (total_euros_on_ride_r[cycle_length] * full_cycles) + total_euros_on_ride_r[remaining_runs]
  
  return total_euros;
    
  

filename = sys.argv[1]

infile = open(filename)

T = int(infile.readline())

for x in range(T):
  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  sys.stdout.write(": ")
  print process_test_case(infile)

infile.close()