import math

def cookieclicker(file):
	f = open(file)
	lines = f.readlines()
	f.close()

	numtests = int(lines[0])
	rest = lines[1:]
	output = ""
	for i in range(numtests):
		numbers = rest[i].split()
		C = float(numbers[0])
		F = float(numbers[1])
		X = float(numbers[2])

		cookies=C
		r=2
		f=0
		time = C/r

		if X<C:
			time = X/2
			output+="Case #"+str(i+1)+": "+str(time)+"\n"
		else:
			j=0
			while j<X:
				# print cookies
				# print time
				# print r+f*F
				# print (X-cookies)/(r+f*F)
				# print (X-cookies+C)/(r+(f+1)*F)
				if (X-cookies)/(r+f*F)<(X-cookies+C)/(r+(f+1)*F):
					cookies+=C
					time+=C/(r+f*F)
				else:
					f+=1
					time+=C/(r+f*F)
				j+=C
			time+=(X-cookies)/(r+f*F)
			output+= "Case #"+str(i+1)+": "+str(time)+"\n"
	return output

print cookieclicker("B-large.in")


