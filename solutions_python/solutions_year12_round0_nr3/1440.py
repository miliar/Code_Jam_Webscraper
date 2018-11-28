# mrtwiddletoes
def rotate(x):
  return x[-1] + x[0:-1]
inp = open('/home/thinkbot/src/random/codejam/C-small-attempt0.in', 'r')
out = open('/home/thinkbot/src/random/codejam/output.out', 'w')
num_trials = int(inp.readline())
for a in xrange(num_trials):
  values = inp.readline().split(' ')
  low = int(values[0])
  high = int(values[1])
  count = 0
  already_used = []
  for num in xrange(low, high):
    test = num
    already_used.append(num)
    for b in xrange(len(str(num))):
      test = int(rotate(str(test)))
      if test >= low and test <= high and sorted([num, test]) not in already_used and num != test:
        count += 1
        already_used.append([num, test])
  out.write('Case #{0}: {1}\n'.format(a+1, count))
