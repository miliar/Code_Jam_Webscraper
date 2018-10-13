def main():
  fh = open("D-large.in", 'r')
  T = int(fh.readline())
  case = 1

  while T > 0:
    getInfo(fh, case)
    T = T -1
    case = case + 1

def getInfo(fh, case):
  num = int(fh.readline())
  values = fh.readline().split()
  values = [int(i) for i in values]
  sorted_vals = sorted(values)
  answer = 0

  for i in range(len(values)):
    if not(values[i] == sorted_vals[i]):
      answer = answer + 1

  print "Case #" + str(case) + ": " + str(answer) + ".000000"

main()
