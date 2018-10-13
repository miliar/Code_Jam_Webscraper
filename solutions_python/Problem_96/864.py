def wo_surprise(i):
  if i < 2:
    return i
  return (i + 2) / 3

def w_surprise(i):
  if i < 2:
    return i
  return (i + 4) / 3

in_file = open('B-large.in')
ncases = int(in_file.readline())

out_file = open('output.txt', 'w')

for case in range(1, ncases + 1):
  line = in_file.readline().split()
  n = int(line[0])
  s = int(line[1])
  p = int(line[2])
  scores = []
  result = 0
  for i in range(0, n):
    scores.append(int(line[3 + i]))
  scores.sort()
  print (n,s,p,scores)
  for i in range(0, n):
    if s == n - i:
      max = w_surprise(scores[i])
      s -= 1
    elif w_surprise(scores[i]) == wo_surprise(scores[i]) or s == 0:
      max = wo_surprise(scores[i])
    elif w_surprise(scores[i]) < p:
      max = wo_surprise(scores[i])
    else:
      max = w_surprise(scores[i])
      s -= 1
    if max >= p:
      result += 1
  print result
  out_file.write('Case #%d: %d\n' % (case, result))
out_file.close()