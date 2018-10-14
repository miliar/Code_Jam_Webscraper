import sys

INPUT_FILE = 'A-large.in'
DEBUG = False



input = open(INPUT_FILE, 'r')
# Read the top line of the file, typically the number of test cases
num_testcases = int(input.readline())

if DEBUG:
  print "Number of test cases:", num_testcases

#for testcase in range(1, 2): # Uncomment to test only one test case
for testcase in range(1, num_testcases + 1): # Uncomment to test all test cases
  test_info = input.readline().split()
  
  tiles = []
  
  num_rows = int(test_info[0])
  num_cols = int(test_info[1])
  
  for r in range(0, num_rows):
    tiles.append([])
    for c in input.readline().strip():
      tiles[r].append(c)
  
  
  
  ### HERE
  ### num_insns is the first number in the test info line
  ### test_info is the list of the rest of the parameters in the info line
  
  if DEBUG:
    print tiles
  
  RESULT = 0
  
  for r in range(0, num_rows):
    for c in range(0, num_cols):
      if tiles[r][c]=='#':
        if c + 1 < num_cols and r + 1 < num_rows and tiles[r][c+1] == '#' and tiles[r+1][c] == '#' and tiles[r+1][c+1] == '#':
          tiles[r][c] = '/'
          tiles[r][c+1] = '\\'
          tiles[r+1][c] = '\\'
          tiles[r+1][c+1] = '/'
        else:
          RESULT = -1
          break
    if RESULT <> 0:
      break
  
  ### /HERE - Put output into RESULT
  
  print "Case #" + str(testcase) + ":"
  if RESULT == -1:
    print "Impossible"
  else:
    for row in tiles:
      for col in row:
        sys.stdout.write(col)
      print ""