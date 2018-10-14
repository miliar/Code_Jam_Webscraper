import sys

if (len(sys.argv) < 2):
  print("No file specified")
  sys.exit(1)
  
infile = open(sys.argv[1])
outfile = open(sys.argv[1] + ".out", "w")

num_cases = int(infile.readline().strip())

for case in range(1, num_cases+1):

  runs, capacity, groups = map(int, map(str.strip, infile.readline().split()))
  groups = map(str.strip, infile.readline().split())
  group_nums = map(int, groups)
  
  total_groups = len(groups)
  
  # Cache of visited states, is a 4-tuple holding
  #   - The next state 
  #   - The money made transferring to the next state
  #   - The result when this state was first encountered
  #   - The runs left when this state was first encountered
  visited_states = {}
  
  result = 0
  state = "-".join(groups)
  
  while runs > 0:
   
    if state in visited_states:
      # We've hit a loop
      _, _, old_result, old_runs = visited_states[state]
      
      loop_size = old_runs - runs
      loop_result = result - old_result
      
      loops_left = runs / loop_size
      
      runs -= loops_left * loop_size
      result += loops_left * loop_result
      
      # There's less than a full loop left but the results should all be in the 
      # cached state now so just run through it.
      while runs > 0:
        new_state, value, _, _ = visited_states[state]
        
        result += value
        runs -= 1
        state = new_state
        
    else:
      # This is a state we haven't seen before so calculate where to go from 
      # here.
      num_groups = 0
      riders = 0
      
      while num_groups < total_groups and group_nums[num_groups] + riders <= capacity:
        riders += group_nums[num_groups]
        num_groups += 1
        
      groups = groups[num_groups:] + groups[:num_groups]
      group_nums = group_nums[num_groups:] + group_nums[:num_groups]
      new_state = "-".join(groups)
      
      visited_states[state] = (new_state, riders, result, runs)
      
      result += riders
      runs -= 1
      state = new_state   
   
  outfile.write("Case #%d: %d\n" % (case, result))
  
  if case % 100 == 0:
    print("Completed case %d" % case)
    
outfile.close()
infile.close()
  
    