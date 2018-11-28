>>> def processLine(a):
	b = a.split(' ')
	for i in range(len(b)):
	    b[i] = int(b[i])
	assert(b[0] == 20)
	c = set(b[1:])
	d = sumdict(c)
	for key in d:
	    if len(d[key]) >= 2:
	        return d[key]

	
>>> def sumdict(s):
	val = dict()
	subsetcount = []
	a = [set()]
	while True:
	    for item in a:
	        if sum(item) in val:
	            val[sum(item)].append(item)
	            return val
	        else:
	            val[sum(item)] = [item]
	    for item in a:
	        subsetcount.append(set(item))
	    b = s.pop()
	    a = list()
	    for item in subsetcount:
	        temp = set(item)
	        temp.add(b)
	        a.append(temp)

>>> def processInput():
	a = input()
	a = a.split('\n')
	for item in range(1, int(a[0])+1):
	    b = processLine(a[item])
	    print("Case #" + str(item) + ":")
	    for thing in b:
	        out = str(thing.pop())
	        for number in thing:
	            put = " " + str(number)
	            out += put
	        print(out)

>>> processInput()
[insert input here and output will be returned]