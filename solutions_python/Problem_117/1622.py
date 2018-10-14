import numpy as np

result = ''
outfile = open("OutputSmall.txt", "w")

with open("InputSmall.txt") as f:
	content = f.readlines()

totalcases = int(content[0])

linecnt = 1

for t in range(0,totalcases):
	result = ''
	oldlinecnt = linecnt
	rowcnt = int(content[linecnt].split(' ')[0].replace('\n',''))
	colcnt = int(content[linecnt].split(' ')[1].replace('\n',''))
	linecnt = linecnt + rowcnt + 1
	print str(rowcnt) + ',' + str(colcnt)
	#rows construction
	rows = []
	for k in range(oldlinecnt + 1, linecnt):
		rows.append(list(content[k].replace(' ','').replace('\n','')))
	
	x = np.array(rows)
	
	rowdict = {}
	l = 0
	for row in rows:
		rowdict[l] = max(row)
		l = l + 1
	#column construction
	columns = x.T
	
	coldict = {}
	n = 0
	for col in columns:
		coldict[n] = max(col)
		n = n + 1	
	
	result = 'YES'
	for i in range(0, rowcnt):
		for j in range(0,colcnt):
			if not(rows[i][j] >= rowdict[i] or rows[i][j] >= coldict[j]): 
				result = 'NO'
				break
	outfile.write('Case #' + str(t + 1) + ': ' + result + '\n')


