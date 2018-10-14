
def combo(combos, LA, top):
  foo = [a[-1] for a in combos if LA in a[:-1] and top in a[:-1] and (LA != top or a[0] == a[1])]
  if foo:
    return foo[0]
  else:
    return None

def opposing(opp, LA, rest):
  for opposing in opp:
    trimmed = ''.join([f for f in opposing if LA != f]) if LA in opposing else None
    if trimmed and any([t for t in rest if t in trimmed]):
      return True
  return False
#  foo = any([1 for a in opp if LA in a and any([t for t in rest if t in a])])
#  return foo

def invokeMagicks(combos, opp, test):
  result = []
  for t in test:
    if result:
      c = combo(combos, t, result[-1])
      if c:
        result.pop()
        result.append(c)
      elif opposing(opp, t, result):
        result = []
      else:
        result.append(t)
    else:
      result.append(t)
#    print result
  return result

def pp(somelist):
  return "[" + ', '.join(somelist) + "]"

def main():
  infile = open("magicka.in", "r", True)
  inputs = infile.readlines()
  tests = int(inputs[0])
  for i in xrange(1,1+tests):
    sequence = inputs[i].strip().split()
    combos = int(sequence[0])
    opposed = int(sequence[combos+1])
    test_length = int(sequence[combos+opposed+2])
    combinations = sequence[1:1+combos]
    opposing = sequence[combos+2:combos+2+opposed]
    test_string = sequence[combos+opposed+3]
#    print combinations, opposing, test_string
    result = invokeMagicks(combinations, opposing, test_string)
    print "Case #%s: %s" % (i, pp(result))

if __name__ == '__main__':
  main()
