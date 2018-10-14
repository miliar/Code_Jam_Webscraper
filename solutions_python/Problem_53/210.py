import sys

if (len(sys.argv) < 2):
  print("No file specified")
  sys.exit(1)
  
infile = open(sys.argv[1])

num_cases = int(infile.readline().strip())

for case in range(1, num_cases+1):

  n, k = map((lambda v: int(v.strip())), infile.readline().split())

  switches = [False for i in range(n)]
  
  for i in range(k):
  
    # idx moves through the array of switches and ends up holding the index of
    # at the final powered switch.
    idx = 0
    
    while idx < n-1 and switches[idx]:
      # This switch is on so there is power to the next switch
      idx += 1
    
    # Flip the switches
    for j in range(idx + 1):
      switches[j] = not switches[j]
      
  result = True
    
  for switch in switches:
    result = result and switch
      
  if result:
    state = "ON"
  else:
    state = "OFF"
    
  print("Case #%d: %s" % (case, state))
    
infile.close()
  
    