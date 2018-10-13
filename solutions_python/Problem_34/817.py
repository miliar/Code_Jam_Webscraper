import os, math
FILENAME = "A-small-attempt3."
#FILENAME = "A-large."
#FILENAME = "alien."
input, output = [], []

#L lowercase letter
#D words

#get input
def clean_read(inpf):
	list = ((inpf.readline()).strip('\n ')).split(' ')
	if len(list) == 1:
		return list[0]
	return list
inpf = open(FILENAME + "in", 'r')
cc = clean_read(inpf)
L = int(cc[0]) #word length
D = int(cc[1]) #word count
N = int(cc[2]) #cases
wlist=[]
clist=[]

#read words
for i in range(D):
	item = clean_read(inpf)
	wlist.append(item)

#hints
for i in range(N):
	item = clean_read(inpf)
	
	#build case
	#print i
	thinger=[]
	j=0
	while j < len(item):
		letter = item[j]
		if letter == '(':
			j += 1
			guy="#"
			while item[j] != ')':
				guy += item[j]
				j += 1
			j += 1
			guy = guy.strip('( )')
			thinger.append(guy)
		else:
			guy=""
			while j < len(item) and item[j] != '(':
				guy += item[j]
				j += 1
			guy = guy.strip('( )')
			thinger.append(guy)
	clist.append(thinger)
inpf.close()


def check_for_word(case, wlist):
	i=0
	idx_list=[]
	for piece in case:
		idx_list.append(i)
		if piece[0] == '#':
			i += 1
		else:
			i += len(piece)
	
	mw_list=[]
	for n in range(len(case)):
		p = case[n]
		th_list=[]
		if p[0] == '#':
			for w in wlist:
				for o in range(1, len(p)):
					if w[idx_list[n]] == p[o]:
						th_list.append(w)
						break
		else:
			for w in wlist:
				if w[idx_list[n]:idx_list[n]+len(p)] == p:
					th_list.append(w)
		mw_list.append(th_list)
	
	#print mw_list
	
	sort_list=[]
	for n in range(len(mw_list)):
		ls = mw_list[n]
		dude = [len(ls), n]
		sort_list.append(dude)
	
	def qsort(listy):
		if len(listy) <= 1:
			return listy
		piv = listy.pop(0)
		ge = qsort([i for i in listy if i[0] >= piv[0]])
		l = qsort([i for i in listy if i[0] < piv[0]])
		return l + [piv] + ge
	
	sort_list = qsort(sort_list)
	#print sort_list
	
	#find all possible words
	it = sort_list[0]
	ix = it[1]
	
	mws = [mw_list[ix]][0][:]
	ansy = mws[:]
	for mw in mws:
		for n in range(len(sort_list)):
			item = sort_list[n]
			if mw not in mw_list[item[1]]:
				ansy.remove(mw)
				break
	return len(ansy)


#solution
for case in clist:
	output.append(check_for_word(case, wlist))
	#print case


#write output
outf = open(FILENAME + "out", 'w')
for i in range(len(output)):
	outf.write("Case #" + str(i+1) + ": " + str(output[i]) + "\n")
outf.close()
