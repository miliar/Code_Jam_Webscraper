import itertools

def get_score(score):
	tp = []
	nsurprise = 0
	mid = score/3
	for i in range(max(mid-2,0),min(mid+3, 11)):
		for j in range(max(mid-2,0), min(mid+3, 11)):
			for k in range(max(mid-2,0), min(mid+3, 11)):
				if i+j+k != score: continue
				t = sorted((i,j,k))
				if t in tp: continue
				if max(t) - min(t) <= 2:
					tp.append(t)
				if max(t) - min(t) == 2:
					nsurprise += 1
	return (tp, nsurprise)

def get_max_score(score_list, sur_on):
	ans = -1
	if sur_on == True:
		for sc in score_list:
			if max(sc) - min(sc) != 2: continue
			if max(sc) > ans: ans = max(sc)
	else:
		for sc in score_list:
			if max(sc) - min(sc) == 2: continue
			if max(sc) > ans: ans = max(sc)
	return ans
	
def run():
	fin = open('b.in', 'r')
	fout = open('b.out', 'w')
	fin.readline()
	c = 1
	for line in fin:
		ql = line.split(' ')
		n = int(ql[0])
		s = int(ql[1])
		p = int(ql[2])
		score = ql[3:]
		max_score = {}
		ids = []
		tot_surprise = 0
		for i in range(n):
			(lst, nsurprise) = get_score(int(score[i]))
			max_score[i] = (get_max_score(lst, True), get_max_score(lst, False))
			if max_score[i][0] > -1:
				ids.append(i)
			tot_surprise += nsurprise
			print lst
		print max_score
		print ids
		ans = 0
		if s == 0:
			for i in range(n):
				if max_score[i][1] >= p:
					ans += 1
		elif tot_surprise == s:
			for i in range(n):
				if i in ids and max_score[i][0] >= p:
					ans += 1
				elif i not in ids and max_score[i][1] >= p:
					ans += 1
		else:
			perm_ids = list(itertools.combinations(ids, s))
			for lst in perm_ids:
				qn = 0
				for i in range(n):
					if i in lst and max_score[i][0] >= p:
						qn += 1
					elif i not in lst and max_score[i][1] >= p:
						qn += 1
				if qn > ans:
					ans = qn
		
		fout.write('Case #%d: %d\n' % (c, ans))
		print '-------'
		c += 1


if __name__ == '__main__':
	run()
