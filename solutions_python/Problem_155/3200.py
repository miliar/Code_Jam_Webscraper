linearray = []

fp = open('A-large.in','r')
for line in fp:
  linearray.append(line.strip('\n'))
fp.close()

outputArray = []
T = int(linearray[0])
for i in range(1, T+1):
  line = linearray[i]

  splits = line.split()
  Smax = int(splits[0])
  shyString = splits[1]

  needed = 0
  totalStanding = int(shyString[0])
  for j in range(1, Smax+1):
    if (totalStanding < j):
    	tmp = (j - totalStanding)
    	totalStanding += int(shyString[j]) + tmp
    	needed += tmp
    else:
    	totalStanding += int(shyString[j])

  outputArray.append("Case #%s: %s\n" % (i, needed))

op = open("first-large.out",'w')
for line in outputArray:
	op.write(line)
op.close()