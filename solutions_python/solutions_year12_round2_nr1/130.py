>>> def processInput():
	a = input()
	a = a.split('\n')
	for i in range(1, int(a[0])+1):
	    b = processLine(a[i])
	    output = "Case #" + str(i) + ":"
	    for item in b:
	        if item > 0:
	            temp = " " + str(item)
	        else:
	            temp = " 0.0"
	        output += temp
	    print(output)

>>> def processLine(line):
	a = line.split(' ')
	b = a[1:]
	a = int(a[0])
	for index in range(a):
	    b[index] = int(b[index])
	distributed = sum(b)
	total = sum(b)*2
	goal = total/a
	finalcontest = b
	switch = True
	while switch:
	    switch = False
	    total = distributed + sum(finalcontest)
	    goal = total/len(finalcontest)
	    b = finalcontest
	    finalcontest = list()
	    for item in b:
	        if goal > item:
	            finalcontest.append(item)
	        else:
	            switch = True
	answerkey = dict()
	for item in finalcontest:
	    answerkey[item] = 100*(goal-item)/distributed
	a = line.split(' ')
	b = a[1:]
	for index in range(int(a[0])):
	    if int(b[index]) in answerkey:
	        b[index] = answerkey[int(b[index])]
	    else:
	        b[index] = 0.0
	return b

>>> processInput()
[copy input here and output will be printed]