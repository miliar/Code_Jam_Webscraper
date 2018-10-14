import sys

def print_result(S):
  for s in (S):
    sys.stdout.write(str(s) + " ")
  print

def consider(first_set, second_set, remaining_values):
  if (len(remaining_values) == 0):
    return False
  if (len(first_set) > 0 and sum(first_set) == sum(second_set)):
    print_result(first_set)
    print_result(second_set)
    return True
  next_value = remaining_values[0]
  next_remaining = remaining_values[1:]
  if (consider(first_set | set([next_value]), second_set, next_remaining)):
    return True
  if (consider(first_set, second_set | set([next_value]), next_remaining)):
    return True
  if (consider(first_set, second_set, next_remaining)):
    return True
  return False

filename = sys.argv[1]

infile = open(filename)

T = int(infile.readline())

for x in range(T):
  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  sys.stdout.write(":")
  print
  
  line = [int(v) for v in infile.readline().split()]
  N = line[0]
  S = line[1:]
  
  if (not consider(set(), set(), S)):
    print "Impossible"
  
infile.close()