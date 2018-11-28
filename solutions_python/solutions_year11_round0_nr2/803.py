import sys

def process_line(line):
  C = int(line[0])
  if (C > 0):
    raw_combinations = line[1:C+1]
  else:
    raw_combinations = []
  D = int(line[C+1])
  if (D > 0):
    oppositions = line[C+2:C+2+D]
  else:
    oppositions = []
  N = line[-2]
  sequence = line[-1]
  
  if (len(sequence) < 2):
    return sequence
  
  combinations = {}
  for i in range(C):
    raw_combination = raw_combinations[i]
    key = raw_combination[0:2]
    value = raw_combination[2]
    combinations[key] = value
    combinations[key[1]+key[0]] = value

  result = sequence[0]
  sequence = sequence[1:]
  
  while (sequence):
    end_combination = ""
    if (len(result) > 0):
      end_combination = result[-1] + sequence[0]
    if (end_combination in combinations):
      result = result[0:-1] + combinations[end_combination]
    else:
      result = result + sequence[0]
    
    for j in range(D):
      if (result.find(oppositions[j][0]) != -1 and result.find(oppositions[j][1]) != -1):
        result = ""
        break;    
    
    sequence = sequence[1:]
  
  return result
  
def format_result(input):
  source = input
  result = "["
  show_comma = 0
  
  while (source):
    if (show_comma):
      result = result + ", "
    result = result + source[0]
    source = source[1:]
    show_comma = 1
  
  result = result + "]"
  return result
    

filename = sys.argv[1]

infile = open(filename)

T = int(infile.readline())

for x in range(T):
  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  sys.stdout.write(": ")
  
  line = [v for v in infile.readline().split()]
  
  print format_result(process_line(line))
  
infile.close()