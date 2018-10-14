import os, math
FILENAME = "B-small-attempt2."
#FILENAME = "B-large."
#FILENAME = "water."
input, output = [], []

rows=0
cols=0
alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

def neighbor_list(r, c, rows, cols):
	qqq=[]
	if r > 0: #n
		t=[]
		t.append(r-1)
		t.append(c)
		qqq.append(t)
	if c > 0: #w
		t=[]
		t.append(r)
		t.append(c-1)
		qqq.append(t)
	if c < cols-1: #e
		t=[]
		t.append(r)
		t.append(c+1)
		qqq.append(t)
	if r < rows-1: #s
		t=[]
		t.append(r+1)
		t.append(c)
		qqq.append(t)
	return qqq[:]

def join_pools(ans, v1, v2):
	for r in range(rows):
		for c in range(cols):
			if ans[r][c] == v1:
				ans[r][c] = v2
	return ans[:][:]

#get input
def clean_read(inpf):
	list = ((inpf.readline()).strip('\n ')).split(' ')
	if len(list) == 1:
		return list[0]
	return list

inpf = open(FILENAME + "in", 'r')
case_cnt = int(clean_read(inpf))
atticus=[]
for i in range(case_cnt):
	rc = clean_read(inpf)
	atticus.append(rc)
	rows = int(rc[0])
	cols = int(rc[1])
	
	#build grid
	grid=[]
	ans=[]
	for r in range(rows):
		a = clean_read(inpf)
		t=[]
		q=[]
		for item in a:
			t.append(int(item))
			q.append(0)
		grid.append(t)
		ans.append(q)
	
	#print grid
	#print ans
	
	z=1
	for r in range(rows):
		for c in range(cols):
			best = []
			nbs = neighbor_list(r, c, rows, cols)
			for nb in nbs:
				if grid[nb[0]][nb[1]] < grid[r][c]:
					if best==[] or grid[nb[0]][nb[1]] < grid[best[0]][best[1]]:
						best = nb[:]
			
			if best != []:
				ro, co = best[0], best[1]
				if ans[r][c] == 0 and ans[ro][co] == 0:
					ans[ro][co] = z
					ans[r][c] = z
					z += 1
				elif ans[r][c] == 0 and ans[ro][co] > 0:
					ans[r][c] = ans[ro][co]
				elif ans[r][c] > 0 and ans[ro][co] == 0:
					ans[ro][co] = ans[r][c]
				else:
					val1, val2 = ans[r][c], ans[ro][co]
					ans = join_pools(ans, val1, val2)
			else:
				if ans[r][c] == 0:
					ans[r][c] = z
					z += 1
				else:
					val1, val2 = ans[r][c], z
					ans = join_pools(ans, val1, val2)
					z += 1
	
	tru_ans=[]
	for r in range(rows):
		tempy=[]
		for c in range(cols):
			tempy.append('?')
		tru_ans.append(tempy)
	
	alph_idx=0
	for r in range(rows):
		for c in range(cols):
			if tru_ans[r][c] == '?':
				compr = ans[r][c]
				for ro in range(rows):
					for co in range(cols):
						if ans[ro][co] == compr:
							tru_ans[ro][co] = alph[alph_idx]
				alph_idx += 1
	
	#output.append(ans)
	output.append(tru_ans)
	
inpf.close()


#write output
outf = open(FILENAME + "out", 'w')
for i in range(len(output)):
	outf.write("Case #" + str(i+1) + ":\n")
	ans = output[i]
	rc = atticus[i]
	for r in range(int(rc[0])):
		for c in range(int(rc[1])):
			if c:
				outf.write(' ')
			outf.write(str(ans[r][c]))
		outf.write('\n')
outf.close()
