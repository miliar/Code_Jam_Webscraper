INPUT_FILE = 'A-small-attempt3.in'
DEBUG = False

def possible(N, Pd):
  x = 100.0 / Pd
  if DEBUG:
    print "x:", x
    
  while not(x==int(x)):
    x = x + (100.0/Pd)
    if DEBUG:
      print "x:", x
    if x > 100:
      x = 100
  if N >= x:
    return "Possible"
  return "Broken"

input = open(INPUT_FILE, 'r')
# Read the top line of the file, typically the number of test cases
num_testcases = int(input.readline())

if DEBUG:
  print "Number of test cases:", num_testcases

#for testcase in range(1, 2): # Uncomment to test only one test case
for testcase in range(1, num_testcases + 1): # Uncomment to test all test cases
  test_info = input.readline().split()
  
  test_info = map(int, test_info)
  N = test_info[0]
  Pd = test_info[1]
  Pg = test_info[2]
  
  ### HERE
  
  if DEBUG:
    #print "Number of instructions / params:", num_insns
    print "Instructions / params:", test_info
    print "N:", N
    print "Pd:", Pd
    print "Pg:", Pg
    
  RESULT = -1
  
  if Pd == 100 and Pg > 0:
    RESULT = "Possible"
  elif Pd == 0 and Pg < 100:
    RESULT = "Possible"
  elif Pd < 100 and Pg == 100:
    RESULT = "Broken"
  elif Pd > 0 and Pg == 0:
    RESULT = "Broken"
  else:
    RESULT = possible(N, Pd)
    

  
  ### /HERE - Put output into RESULT
  
  print "Case #" + str(testcase) + ":", RESULT