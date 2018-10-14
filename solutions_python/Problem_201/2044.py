from math import floor, ceil, log;
T = int(raw_input());
for i in xrange(1, T + 1):
  stringVar = raw_input().split(' ');
  N = int(stringVar[0]);
  K = int(stringVar[1]);
  spaces = [N];
  height = int(log(K, 2));
  for j in xrange(0, height):
    new = [];
    for k in xrange(0, len(spaces)):
      temp = spaces[k];
      left = (temp - 1) // 2;
      right = temp - 1 - left;
      new.append(left);
      new.append(right);
    spaces = new;

  rest = K - 2**height;

  given = sorted(spaces, reverse=True)[rest];
  left = (given - 1) // 2;
  right = given - 1 - left;
  print "Case #{}: {} {}".format(i, right, left);