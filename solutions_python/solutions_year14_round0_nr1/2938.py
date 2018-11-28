def read_matrix():
  return [map(int, raw_input().split(' ')) for i in xrange(4)]

def read_int():
  return int(raw_input())

def intersect(arr1, arr2):
  return [x for x in arr1 if x in arr2]

def solve(case):
  row1 = read_int()-1
  m1 = read_matrix()
  row2 = read_int()-1
  m2 = read_matrix()
  
  i = intersect(m1[row1], m2[row2])
  
  ans = ""

  if len(i) == 0:
    ans = "Volunteer cheated!"
  elif len(i) > 1:
    ans = "Bad magician!"
  else:
    ans = "%d" % i[0];

  print "Case #%d: %s" % (case, ans)


T = int(raw_input())
for i in xrange(1,T+1): solve(i)


