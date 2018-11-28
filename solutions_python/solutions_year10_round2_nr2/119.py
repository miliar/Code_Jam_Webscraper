
fin = '1.in'
#fin = 'A-small-attempt0.in'
#fin = 'A-large.in'
fin = 'B-large.in'
fout= fin + '.out'

f=open(fin, 'r')
fo=open(fout, 'w')
T = int(f.readline())

for t in range(1, T+1):
	s = f.readline()
	N = int(s.split(' ')[0])
	K = int(s.split(' ')[1])
	B = int(s.split(' ')[2])
	T = int(s.split(' ')[3])
	pos = [int(tmp) for tmp in f.readline().split()]
	spd = [int(tmp) for tmp in f.readline().split()]
#	print pos, spd
	cnt = 0
	ans = 0
	for i in range(len(pos) - 1, -1, -1):
		if pos[i] + spd[i] * T >= B:
			cnt+=1
			if cnt >= K:break
		else:
			if cnt < K:
				ans+=K-cnt
	rs = ''
	if cnt < K:
		rs = 'IMPOSSIBLE'
	else: rs = str(ans)
	print 'Case #'+str(t)+ ': ' + rs
	fo.write('Case #'+str(t)+ ': ' + rs + '\n')
