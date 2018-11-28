def findFlips(S, K):
  firstBlank = S.find('-');
  if firstBlank != -1:
    rest = S[firstBlank:];
    if len(rest) < K:
      return "IMPOSSIBLE";
    rest = flip(rest, K);
    next = findFlips(rest, K);
    if next == "IMPOSSIBLE":
      return next;
    else:
      return 1 + next;
  else:
    return 0;

def flip(s, K):
  sList = list(s);
  for i in xrange(0, K):
    if sList[i] == "+":
      sList[i] = "-";
    else:
      sList[i] = "+";
  new = "".join(sList);
  return new;

T = int(raw_input())
for i in xrange(1, T + 1):
  caseVar = raw_input().split(' ');
  S = caseVar[0];
  K = int(caseVar[1]);
  count = findFlips(S, K);
  print "Case #{}: {}".format(i, count);


