
def check(lif, nf, kf):
	ans = 0
	for i in range(nf):
		if(lif[i] == '-'):
			if((i+kf) <= nf):
				ans +=1
				for t in range(i,i+kf):
					if(lif[t] == '+'):
						lif[t] = '-'
					else:
						lif[t] = '+'
		# print lif
	ch = 1
	for i in range(nf):
		if(lif[i] == '-'):
			ch = 0
			break
		# print lif
	return (ch,ans)

t = int(raw_input())
for i in range(t):
	l = raw_input().split()
	n = len(l[0])
	li = list(l[0])
	# print li[0] == '+'
	k = int(l[1])
	tes = check(li, n, k)
	if(tes[0]==1):
		print "Case #{}: {}".format(i+1, tes[1])
	else:
		print "Case #{}: {}".format(i+1, "IMPOSSIBLE")