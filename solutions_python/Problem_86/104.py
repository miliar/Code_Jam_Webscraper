#import sys
import math

INPUT_FILE = 'C-small-attempt3.in'
DEBUG = False



input = open(INPUT_FILE, 'r')
# Read the top line of the file, typically the number of test cases
num_testcases = int(input.readline())

if DEBUG:
  print "Number of test cases:", num_testcases

#for testcase in range(1, 2): # Uncomment to test only one test case
for testcase in range(1, num_testcases + 1): # Uncomment to test all test cases
  test_info = map(int, input.readline().split())
  
  N = test_info[0]
  L = test_info[1]
  H = test_info[2]
  
  freqs = map(int, input.readline().split())
  
  RESULT = "NO"
  
  for poss in range(L, H + 1):
    #if poss in freqs:
    #  continue
  
    count = 0
    for f in freqs:
      if f % poss == 0 or poss % f == 0:
        count = count + 1
    if count == N:
      RESULT = poss
      break
  
  ### /HERE - Put output into RESULT
  
  print "Case #" + str(testcase) + ":", RESULT