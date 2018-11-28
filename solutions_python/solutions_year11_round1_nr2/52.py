# Question B
# By Simulation of Word Scoring
# Ameer Ayoub <ameer.ayoub@gmail.com>
from copy import copy

def cw(w, ch, pos):
	r_list = []
	isok = False
	# word, char, open positions
	for i in range(len(w)):
		if i in pos and w[i] == ch:
			isok = True
			r_list.append(i)
	return (isok, r_list)

def cl(ch, op, dc):
	for wd in dc:
		if cw(wd, ch, op)[0]:
			return True
	return False
	
def sw(w, l, d):
	op = range(len(w))
	# word, list, dict
	points = 0
	dc = copy(d)
	
	# remove all mismatch length words
	nd = copy(dc)
	for wd in dc:
		if len(wd) != len(w):
			nd.remove(wd)
	dc = nd
	#print dc
	
	for ch in l:
		#print ch, ":", dc
		if len(op) > 0 and cl(ch, op, dc):
			# guess that letter!
			# check if actually in word
			if cw(w, ch, range(len(w)))[0] == False:
				#print ch
				points += 1
				nd = copy(dc)
				for wd in dc:
					check = cw(wd, ch, op)
					if check[0]:
						nd.remove(wd)
				dc = nd
			else:
				these_pos = []
				for pos in cw(w, ch, range(len(w)))[1]:
					these_pos.append(pos)
					op.remove(pos)
				nd = copy(dc)
				for wd in dc:
					check = cw(wd, ch, range(len(wd)))
					if not these_pos == check[1]:
						nd.remove(wd)
				dc = nd
	return points
	
f = open("B.in")
t = int(f.readline())
for _t in range(t):
	n, m = map(int, f.readline().split())
	dic = []
	for _n in range(n):
		dic.append(f.readline()[:-1])
	#print dic
	winners = []
	for _m in range(m):
		max_word = ""
		max_score = -1
		wl = list(f.readline()[:-1])
		#print len(wl), wl
		for wd in dic:
			score = sw(wd, wl, dic)
			if score > max_score:
				max_score = score
				max_word = wd
		winners.append(max_word)
	buffer = ""
	buffer += "Case #{0}:".format(_t+1)
	for word in winners:
		buffer += " {0}".format(word)
	print buffer