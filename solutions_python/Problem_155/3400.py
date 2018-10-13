import sys

def _process_input(case, str_input):
  splitted = str_input.split(' ')
  smax = splitted[0]
  audience = splitted[1]

  stand_up = 0
  added = 0
  s_index = 0
  for s in audience: 
    s_int = int(s)
    if(s_int != 0):
      diff = stand_up - s_index
      if diff < 0:
        to_be_added = 0 - diff
        stand_up = stand_up + to_be_added
        added = added + to_be_added
      stand_up = stand_up + s_int
    s_index = s_index + 1

  print("Case #%d: %d"%(case, added))

if __name__ == '__main__':
  with open(sys.argv[1], 'r') as f:
    t = f.readline().strip()

    case = 1
    for line in f:
      _process_input(case, line.strip('\n'))
      case = case + 1