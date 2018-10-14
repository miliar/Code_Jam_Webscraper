>>> def processLine(line):
	a = line.split(' ')
	N = int(a[0])
	S = int(a[1])
	p = int(a[2])
	surprising = 0
	notsurprising = 0
	if p >= 2:
	    bound1 = 3*p-2
	    bound2 = 3*p-4
	elif p == 1:
	    bound1 = 1
	    bound2 = 1
	elif p == 0:
	    bound1 = 0
	    bound2 = 0
	for i in range(3, len(a)):
	    k = int(a[i])
	    if k >= bound1:
	        notsurprising += 1
	    elif k >= bound2:
	        surprising += 1
	answer = notsurprising
	if S >= surprising:
	    answer += surprising
	else:
	    answer += S
	return answer

>>> def answer():
	a = input()
	b = a.split('\n')
	k = int(b[0])
	for i in range(1,k+1):
	    print("Case #" + str(i) + ": " + str(processLine(b[i])))

>>> answer()
[Insert input here]
[Output will print]