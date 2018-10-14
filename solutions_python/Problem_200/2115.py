def findLast(l):
  for i in xrange(len(l) - 1, 0, -1):
    if l[i] < l[i-1]:
      return i;
  return False;

def findTidy(l):
  last = findLast(l);
  if last == False:
    return "".join(l);
  else:
    l[last-1] = str(int(l[last-1]) - 1);
    return "".join(findTidy(l[:last])) + ('9'*(len(l) - last));

T = int(raw_input());
for i in xrange(1, T + 1):
  N = raw_input();
  Nlist = list(N);
  result = findTidy(Nlist);
  if result[0] == '0':
    print "Case #{}: {}".format(i, result[1:]);
  else:
    print "Case #{}: {}".format(i, result);