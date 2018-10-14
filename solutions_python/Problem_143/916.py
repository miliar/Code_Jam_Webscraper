fo = open("input2","r")
fw = open("output","w")

def stoint(s):
        return int(s.strip())

c = fo.readline()
c = stoint(c)
results = []

for i in range(0,c):
	temp = fo.readline()
	temp = temp.strip()
	temp = temp.split()
	a = int(temp[0])
	b = int(temp[1])
	k = int(temp[2])
	count = 0
	for j in range(0,a):
		for l in range(0,b):
			if j & l < k:
				count = count +1
	
	results.append(count)			

print results
for i in range(0,len(results)):
	fw.write("Case #{0}: {1}\n".format( i+1, results[i]))
