def result(filename):
  lines = [line.strip() for line in open(filename)]
  for x in range(1,int(lines[0])+1):
    answer = str(needed(lines[x]))
    print "Case #"+ str(x)+ ": " + answer

#x


def needed(line):
  total = 0
  worstDiff = 0
  for x in range(2,(int(line[0])+3)):
    needed = x-2
    difference = needed - total
    if (difference > worstDiff):
      worstDiff = difference
    total = total + int(line[x])
  return worstDiff

result("input1.txt")