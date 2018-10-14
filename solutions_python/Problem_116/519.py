import sys

def get_record():
  result = {}
  result['X'] = 0
  result['O'] = 0
  return result
  
def get_four_records():
  result = []
  result.append(get_record())
  result.append(get_record())
  result.append(get_record())
  result.append(get_record())
  return result
  
def add_to_record(record, c):
  if (c == 'T'):
    record['X'] += 1
    record['O'] += 1
  else:
    record[c] += 1  

def print_winner(record):
  if (record['X'] == 4):
    sys.stdout.write("X won")
    return 1
  elif (record['O'] == 4):
    sys.stdout.write("O won")
    return 1
  else:
    return 0
  
def run_case(infile):
  rows = get_four_records()
  cols = get_four_records()
  diagonal_lr = get_record()
  diagonal_rl = get_record()
  open_count = 0
  
  for j in range(4):
    row = infile.readline().strip()
    for i in range(4):
      c = row[i]
      if (c == '.'):
        open_count += 1
      else:
        add_to_record(rows[j], c)
        add_to_record(cols[i], c)
        if (i == j):
          add_to_record(diagonal_lr, c)
        if (i + j == 3):
          add_to_record(diagonal_rl, c)
  
  for row in rows:
    if (print_winner(row)):
      return
      
  for col in cols:
    if (print_winner(col)):
      return
      
  if (print_winner(diagonal_lr)):
    return
    
  if (print_winner(diagonal_rl)):
    return;
  
  if (open_count):
    sys.stdout.write("Game has not completed")
  else:
    sys.stdout.write("Draw")


filename = sys.argv[1]

infile = open(filename)

T = int(infile.readline())

for x in range(T):
  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  sys.stdout.write(": ")
  
  run_case(infile)
  
  print
  infile.readline()
  
  
  
infile.close()