dic = {'z' : 'q', 'q' : 'z'}
in1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
in2 = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
in3 = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'

out1 = 'our language is impossible to understand'
out2 = 'there are twenty six factorial possibilities'
out3 = 'so it is okay if you want to just give up'

for i in range(len(in1)):
	dic [in1 [i]] = out1 [i]
	dic [in2 [i]] = out2 [i]
	dic [in3 [i]] = out3 [i]


f = open("A-small-attempt1.in", "r")
w = open("out.txt", "w")
in4 = f.readline()
N = int(in4)
for i in range(N):
	in4 = f.readline()
	out = ''
	for j in in4:
		if j in dic.keys():
			out = out + dic [j]
	w.write("Case #" + str(i + 1) + ": " + out + "\n")
