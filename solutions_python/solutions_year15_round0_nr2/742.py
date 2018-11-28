import sys

with open("B-large.in") as f:
  num_cases = int(f.readline().strip())
  for case in range(num_cases):
    f.readline()
    data = [int(datum) for datum in f.readline().split()]
    
    best_time = 10**20
    for stack_size in range(1, max(data)+1):
      moves_required = 0
      for d in data:
        moves_required += ((d-1-stack_size)/stack_size)+1
      if moves_required + stack_size < best_time:
        best_time = moves_required + stack_size
        
    
    print("Case #{}: {}".format(case+1,best_time))