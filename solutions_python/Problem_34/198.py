infile = open('/home/patanjali/Desktop/A-large.in')
outfile = open('A-large.out','w')

nums = infile.readline()

L, D, N = nums.strip().split(' ')

dictionary, regexes = [], []

for i in xrange(int(D)):
  dictionary.append(infile.readline().strip())

for i in xrange(int(N)):
  regexes.append(infile.readline().strip())

print dictionary

print regexes
## Creating the regexdict
for index, x in enumerate(regexes):
  ts = []
  while(x != ''):
    start, end = x.find('('), x.find(')')
    if start == -1:
      ts.extend(list(x))
      x = ''
    else :
      if x[0:start]:
	ts.extend(list(x[0:start]))
      if x[start+1:end]:
	ts.append(x[start+1:end])
      x = x[end+1:]
    regexes[index] = ts

print regexes

counts = []

for regex in regexes:
  counts.append(0)
  for word in dictionary:
    for x, y in zip(list(word), regex):
      if x not in y:
	print x, "not in", y
	break
    else:
      print "Matched", word, regex
      counts[-1] += 1

for i, count in enumerate(counts):
  outfile.write("Case #%s: %s\n" %(i+1, count))

infile.close()
outfile.close()