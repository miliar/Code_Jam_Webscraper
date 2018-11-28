
def compute(s):
	count = [0]*26
	for character in s:
		count[ord(character)-65] += 1

	final = []

	z = count[25]
	temp = [0]*z
	final.extend(temp)


	w = count[22]
	temp = [2]*w
	final.extend(temp)
	
	u = count[20]
	temp = [4]*u
	final.extend(temp)
	
	x = count[23]
	temp = [6]*x
	final.extend(temp)
	
	g = count[6]
	temp = [8]*g
	final.extend(temp)

	count[25] -= z
	count[4] -= (z+g)
	count[17] -= (z+u)
	count[14] -= (z+w+u)
	count[19] -= (w+g)
	count[22] -= w
	count[5] -= u
	count[20] -= u
	count[18] -= x
	count[8] -= (x+g)
	count[23] -= x
	count[6] -= g
	count[7] -= g

	o = count[14]
	temp = [1]*o
	final.extend(temp)

	t = count[19]
	temp = [3]*t
	final.extend(temp)

	f = count[5]
	temp = [5]*f
	final.extend(temp)

	s = count[18]
	temp = [7]*s
	final.extend(temp)


	count[14] -= o
	count[13] -= (o+s)
	count[4] -= (o+t+t+f+s)
	count[19] -= t
	count[7] -= t
	count[17] -= t
	count[5] -= f
	count[8] -= f
	count[21] -= (f+s)
	count[18] -= s
	count[4] -= s

	i = count[8]
	temp = [9]*i
	final.extend(temp)

	final.sort()

	final_s = ''.join(str(e) for e in final)


	return final_s









filename = "A-large (1).in"
f = open(filename, "r")
content = [x.strip('\n') for x in f.readlines()]
f.close()


f = open("output_digits.out","w+")
flag = 0

for i,x in enumerate(content[1:]):
	flag = compute(x)
	f.write("Case #" + str(i+1) + ": " + flag + "\n")
	

f.close()
