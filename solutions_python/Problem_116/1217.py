
def z(x):
  if 0 <= x <= 3:
    return x
  raise

def test(case, i, j):
  x = case[i][j]
  if x in ('.', 'T'):
    return False
  d, l = [], []
  for k in range(-3, 4):
    try:
      d.append(case[z(i-k)][z(j)])
    except:
      continue
  l = [y for y in d if y in (x, 'T')]
  # print('vertical')
  # print(d)
  if len(l) == 4:
    return x

  d, l = [], []
  for k in range(-3, 4):
    try:
      d.append(case[z(i-k)][z(j-k)])
    except:
      continue
  l = [y for y in d if y in (x, 'T')]
  # print('diagonal')
  # print(d)
  if len(l) == 4:
    return x

  d, l = [], []
  for k in range(-3, 4):
    try:
      d.append(case[z(i-k)][z(j+k)])
    except:
      continue
  l = [y for y in d if y in (x, 'T')]
  # print('diagonal')
  # print(d)
  if len(l) == 4:
    return x

  d, l = [], []
  for k in range(-3, 4):
    try:
      d.append(case[z(i)][z(j-k)])
    except:
      continue
  l = [y for y in d if y in (x, 'T')]
  # print('horizontal')
  # print(d)
  if len(l) == 4:
    return x
    

if __name__ == '__main__':
  import sys
  args = sys.argv[1:]
  if not args:
    exit(0)
  file = open(args[0], 'r')
  # for line in file.readlines():
  case_count = int(file.readline().strip())
  for n in range(1, case_count+1):
    case = []
    for i in range(4):
      case.append(file.readline().strip())
    file.readline()
    result = [test(case, i, j) for i in range(4) for j in range(4)]
    if 'X' in result:
      print('Case #{}: X won'.format(n))
      continue
    if 'O' in result:
      print('Case #{}: O won'.format(n))
      continue
    if any('.' in l for l in case):
      print('Case #{}: Game has not completed'.format(n))
      continue
    print('Case #{}: Draw'.format(n))
    
