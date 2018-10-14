from copy import copy
scores_n = map(lambda x:-1, range(31))
scores_s = copy(scores_n)

for i in range(11):
    for j in range(i, i+3):
	for k in range(i, i+3):
	    score = i + j + k
	    if score>30 or j>10 or k>10:
		continue
	    if j==i+2 or k==i+2:
		if max([i,j,k])>scores_s[score]:
		    scores_s[score] = max([i,j,k])
	    else:
		if max([i,j,k])>scores_n[score]:
		    scores_n[score] = max([i,j,k])

for i in range(31):
    if scores_s[i]==-1:
	scores_s[i]=scores_n[i]

# Start Calculate
fn = 'B-large'
fi = open('%s.in' % fn, 'r')
fo = open('%s.out' % fn, 'w')
t = int(fi.readline())
cases = fi.readlines()
fi.close()

for c in range(t):
    ns = map(lambda x: int(x), cases[c].strip().split(' '))
    n = ns[0]
    s = ns[1]
    p = ns[2]
    gs = ns[3:3+n]
    target = 0
    for g in gs:
	if scores_n[g]>=p:
	    target = target + 1
	    continue
	if s>0 and scores_s[g]>=p:
	    target = target + 1
	    s = s - 1
	    continue
    fo.write("Case #%s: %s\n" % ((c+1),target))

fo.close()
