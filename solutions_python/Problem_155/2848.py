# Standing Ovation
# by Walter Smuts

#Input
f = open(input("Enter file name: "), "r")

#Processing
c = int(f.readline())
o = open("output.txt", "w")

for i in range(c):
	add = 0
	t = 0
	s = f.readline()
	m = s[:s.find(' ')]
	s = s[s.find(' ')+1:]
	
	for c in range(int(m)+1):
		if c > t:
			add += c - t
			t += c - t
		t += int(s[c])
	o.write('Case #'+ str(i+1) + ': ' + str(add) + '\n')

#End
f.close()
o.close()
