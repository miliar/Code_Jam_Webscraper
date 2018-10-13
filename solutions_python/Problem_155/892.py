import fileinput

def dosomething(shy):
	ans = 0
	now = 0
	for i in range(len(shy)):

		if now >= i:
			now += int(shy[i])
		else:
			ans += i - now
			now += (i - now) + int(shy[i])
	return ans


fin = open("q1.in","r")
fout = open("q1.out","w")

n = int (fin.readline())
lines = list(fin)
#print (lines)

for i in range(n):
	#print (lines[i][2:-1])
	line =  lines[i].split()[1]
	print (line)
	fout.write("Case #" + repr(i + 1) + ": " + \
	 repr(dosomething(line)) + "\n")



#print (n)

