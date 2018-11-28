def check_applause(n, l):
	total = 0
	friends = 0
	for i in range(len(l)):
		#print i, str[i], total, friends
		if total >= i:
			total += int(l[i])
		elif int(l[i]) > 0:
			friends = friends + (i - total)
			total = i + int(l[i])
		#print i, str[i], total, friends
	return friends

f = open("A-large.in", "r")
r = open("output.txt", "w")
n = f.readline()
n = n.rstrip()
n = int(n)
for i in range(n):
	content = f.readline()
	content = content.rstrip()
	content = content.split(" ")
	k = int(content[0])
	string = content[1]
	answer = check_applause(k, string)
	r.write("Case #" + str(i+1)+": "+str(answer) + "\n") 

f.close()
r.close()