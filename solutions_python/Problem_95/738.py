s = "yhesocvxduiglbkrztnwjpfmaq"
n = int(raw_input())
for i in range(n):
	print "Case #%d:" % (i+1),
	t = ""
	p = raw_input()
	for j in p:
		if j==' ':
			t += ' '
		else:
			t += s[ord(j)-ord('a')]
	print t
