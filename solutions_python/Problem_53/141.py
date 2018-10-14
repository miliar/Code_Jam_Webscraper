
def solve(line):
  n = int(line[0])
  k = int(line[1])

  limit = pow(2,n)
  if k%limit == limit-1:
    return "ON"
  else:
    return "OFF"

if __name__ == "__main__":
  i = 0
  for line in open("A-large.in"):
    if i > 0:
      line1 = line.split()
      print "Case #%s: %s" % (i, solve(line1))
    i += 1