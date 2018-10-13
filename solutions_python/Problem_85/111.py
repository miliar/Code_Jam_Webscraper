import sys

INPUT_FILE = 'B-small-attempt0.in'
DEBUG = False



input = open(INPUT_FILE, 'r')
# Read the top line of the file, typically the number of test cases
num_testcases = int(input.readline())

if DEBUG:
  print "Number of test cases:", num_testcases

#for testcase in range(1, 2): # Uncomment to test only one test case
for testcase in range(1, num_testcases + 1): # Uncomment to test all test cases
  test_info = map(int, input.readline().split())
  
  L = test_info[0] # Number of boosters possible
  t = test_info[1] # Time to build a booster
  N = test_info[2] # Destination star
  C = test_info[3] # Number of star distances
  dists = test_info[4:]


  # CODE HERE
  RESULT = -1
  
  space = range(0, N)
  for i, s in enumerate(space):
    space[i] = dists[i % C]

  if L == 0:
    RESULT = sum(map(lambda x: x*2, space))
    print "Case #" + str(testcase) + ":", RESULT
    continue
  
  sunk_cost_dist = t / 2
  while sunk_cost_dist > 0:
    if space[0] < sunk_cost_dist:
      sunk_cost_dist = sunk_cost_dist - space[0]
      del space[0]
    else:
      space[0] = space[0] - sunk_cost_dist
      sunk_cost_dist = 0
  
  time_traveled = t
  
  # Now that we have traveled t / 2 parsecs, the speed boosters can finish.
  # We want to put them on the largest legs of the journey
  # REMEMBER: THEY MUST BE ON DIFFERENT STARS!
  space.sort()
    
  for booster in range(0, L):
    time_traveled = time_traveled + space.pop()
  
  time_traveled = time_traveled + sum(map(lambda x: x*2, space))
  
  RESULT = time_traveled
  
  print "Case #" + str(testcase) + ":", RESULT