import sys

def check(line):
  a = list(line)
  i = 0
  check_for = a[0]
  if check_for == 'T':
    check_for = a[1]
  count = a.count(check_for)
  if count < 3 or '.' in a:
    return False
  elif (count == 4) or (count == 3 and 'T' in a):
    return check_for

def not_comp(case):
  for line in case:
    for char in line:
      if char == '.':
        return True
  return False


def main(fname):
  fin = open(fname)
  cases = int(fin.readline().strip())
  lines = []
  for line in fin:
    line = line.strip()
    if line != '':
      lines.append(line)


  for i in xrange(cases):
    case = lines[i*4:(i*4)+4]

    #create a list of hor, vert, diag to check
    #hor
    check_list = case
    #vert
    for a in xrange(4):
      line = ''
      for b in xrange(4):
        line += case[b][a]
      check_list.append(line)
    #diag
    d1 = case[0][0] + case[1][1] + case[2][2] + case[3][3]
    d2 = case[0][3] + case[1][2] + case[2][1] + case[3][0]
    check_list.append(d1)
    check_list.append(d2)
    won = 0
    for line in check_list:
      if check(line) == 'X' or check(line) == 'O':
        ch = check(line)
        print 'Case #%d: %s won' % (i+1, ch)
        won = 1
        break
    if won == 1:
      continue
    elif not_comp(case):
      print 'Case #%d: Game has not completed' % (i+1)
      continue
    print 'Case #%d: Draw' % (i+1)


if __name__ == '__main__':
  main(sys.argv[1])
