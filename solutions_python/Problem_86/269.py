#fi = open('C-test.in','r')
fi = open('C-small-attempt0.in','r')
fo = open('A-small.out','w')

T = int(fi.readline().strip())
for t_no in range(1,T+1):
	N,L,H = [int(x) for x in fi.readline().split(' ')]
	note = [int(x) for x in fi.readline().split(' ')]
	for i in range(L,H+1):
		check = 1
		for x in note:
			if x<i:
				check = i%x
			else:
				check = x%i
			if check != 0:
				break
		if check == 0:
			fo.write("Case #%d: %d\n" % (t_no,i))
			break
	if check != 0:
		fo.write("Case #%d: NO\n" % (t_no))
	
fi.close()
fo.close()