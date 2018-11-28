
def main():
  dbg = False
  #f = open('A-sample.txt', 'r')
  f = open('A-small-attempt0.in', 'r')
  data = f.readlines()
  T = int(data[0])
  case = 1
  line = 1
  while case <= T:
    row1 = int(data[line])
    num1 = set([int(x) for x in data[line + row1].split()])
    line += 5
    row2 = int(data[line])
    num2 = set([int(x) for x in data[line + row2].split()])
    line += 5

    if (dbg): print "============================================"
    if (dbg): print row1, num1
    if (dbg): print row2, num2
    if (dbg): print num1 & num2
    if (dbg): print "============================================"

    number = num1 & num2
    if len(number) == 1:
      solution = "%d" % number.pop()
    elif len(number) == 0:
      solution = "Volunteer cheated!"
    else:
      solution = "Bad magician!"

    print "Case #%d: %s" % (case, solution)
    case += 1

if __name__ == "__main__":
    main()
