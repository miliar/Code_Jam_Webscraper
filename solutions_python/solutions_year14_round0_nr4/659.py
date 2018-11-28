def bigger(n, num):
	for a in range(len(n)):
		if n[a] > num:
			return a
	return len(n)-1

def war(n, k):
	c = 0
	for a in range(len(n)):
		if n[len(n)-1] > k[len(k)-1]:
			n = n[:len(n)-1]
			k = k[1:]
			c+=1
		else:
			ind = bigger(k, n[len(n)-1])
			n = n[:len(n)-1]
			k = k[:ind] + k[ind+1:]
	return c

def dwar(n, k):
	c = 0
	for a in range(len(n)):
		if n[0] > k[0]:
			n = n[1:]
			k = k[1:]
			c+=1
		else:
			n = n[1:]
			k = k[:len(k)-1]
	return c

f = open("/Users/mklein16/Desktop/gcj/D-large.in", 'r')
contents = f.read()
cases = int(contents.split("\n")[0])
contents = contents.split("\n")
for i in range(cases):
	content = []
	for a in range(3):
		content.append(contents[1+a+i*3])
	naom = content[1].split(" ")
	ke = content[2].split(" ")
	naomi = []
	ken = []
	for a in range(int(content[0])):
		naomi.append(float(naom[a]))
		ken.append(float(ke[a]))
	naomi.sort()
	ken.sort()
	w = war(naomi, ken)
	d = dwar(naomi, ken)
	f.close()
	g = open("/Users/mklein16/Desktop/gcj/output.txt", 'a')
	g.write("Case #" + `i+1`+": " + `d` + " " + `w` + "\n")
	g.close()