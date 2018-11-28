
def gs(f):
  g = int(f.readline())
  assert 1 <= g and g <= 4
  s1 = [f.readline() for j in xrange(4)][g-1]
  s1 = set([int(i) for i in s1.split() if i])
  assert len(s1) == 4
  return s1

def guess(f):
  s1 = gs(f)
  s2 = gs(f)
  result = s1.intersection(s2)
  if len(result) == 1:
    return result.pop()
  elif len(result) > 1:
    return "Bad magician!"
  else:
    return "Volunteer cheated!"

def main(filename):
  with open(filename) as f:
    t = int(f.readline())
    for i in xrange(t):
      print "Case #{}: {}".format(i+1, guess(f))

if __name__ == '__main__':
  main('A-small-attempt0.in')
