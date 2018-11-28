T = input();
f = open("output", "w")
for i in range(T):
	sent = raw_input()
	d = sent.split(" ");
	N = int(d[0])
	S = int(d[1])
	p = int(d[2])
	t = d[3 : 3+N]
	r = 0
	if S > 0 :
		for j in range(0, N):
			if int(t[j]) in ((p*3-3),(p*3-4)):
				if int(t[j]) >= 2:
					r = r + 1
					print('* '+t[j] + ' ' + str(r))
		if r > S :
			r = S
	for j in range(0, N):
		if int(t[j]) >= (p*3-2):
			r = r + 1
			print(t[j] + ' ' + str(r))
	f.write('Case #' + str(i+1) + ': ' + str(r) + '\n')
