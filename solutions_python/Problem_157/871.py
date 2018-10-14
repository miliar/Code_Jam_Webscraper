import sys

input_file = open(sys.argv[1], "r")
output_file = open(sys.argv[2], "w")

def k():
  return False

RESULT = [2,3,4]

BOOLMAP = {
  True: "YES\n",
  False: "NO\n"
}

# map of quarternions to numbers
QMAP = {
  "1": 1,
  "i": 2,
  "j": 3,
  "k": 4
}

# table of rules for multiplying quarternions
RULES = {
  (1,1): 1,
  (1,2): 2,
  (1,3): 3,
  (1,4): 4,

  (2,1): 2,
  (2,2): -1,
  (2,3): 4,
  (2,4): -3,

  (3,1): 3,
  (3,2): -4,
  (3,3): -1,
  (3,4): 2,

  (4,1): 4,
  (4,2): 3,
  (4,3): -2,
  (4,4): -1
}

# function for reduction
def f(x,y): return x or y

# function to multiply quarternions (handles negativity)
def mult(x,y):
  if ((x < 0) and (y < 0)):
    return RULES[(abs(x),abs(y))]
  elif ((x < 0) or (y < 0)):
    return -RULES[(abs(x),abs(y))]
  else:
    return RULES[(x,y)]

def convert(s):
  result = []
  for i in range(len(s)):
    result.append(QMAP[s[i]])
  return result

def naive(s):
  return (reduce(mult,s) == -1)

def solve(s, i):
  if (i == len(RESULT)):
    return True
  ss_Indices = find(RESULT[i], s)
  if (len(ss_Indices) != 0):
    for index in range(len(ss_Indices)):
      if (solve(s[ss_Indices[index]:], (i+1))):
        return True
    return False
  else:
    return False

# function to find the value v by multiplying through s.
# should return a pair: (boolean, followed by substring cutoff)
def find(v, s):
  currVal = 1
  result = []
  for i in range(len(s)):
    currVal = mult(currVal, s[i])
    if (currVal == v):
      result.append(i + 1)
  return result

try:
  num_cases = int(input_file.readline())
  for case in range(num_cases):
    case_response = "Case #%d: " % (case+1)
    curr_case_info = input_file.readline().split()
    curr_case_str = input_file.readline()
        
    curr_l = int(curr_case_info[0])
    curr_x = int(curr_case_info[1])
    curr_case_str = ''.join(curr_case_str.split())
    curr_case_str *= curr_x
    representation = convert(curr_case_str)

    if (((curr_x * curr_l) < len(RESULT)) or 
       (not naive(representation))):
      case_response += BOOLMAP[False]
    else:
      case_response += BOOLMAP[solve(representation, 0)]
    
    output_file.write(case_response)

finally:
  input_file.close()
  output_file.close()