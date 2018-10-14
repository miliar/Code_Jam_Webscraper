
def toggle(x):
	i = [j for j in x]
	for j in range(len(i)):
		if i[j]=='-':i[j]='+'
		else: i[j]='-'
	return ''.join(i)

def flipPancakes(row,flipperSize):
    flip = 0
    while row.count('+') < len(row):
        ind = row.find('-')
        flip+=1
        if ind+flipperSize> len(row): break
        temp = row[ind:ind+flipperSize]
        #print temp
        temp = toggle(temp)
        #print temp
        row=row[:ind]+temp+row[ind+flipperSize:]
        #print row
        if flip ==len(row): break

    if row.count('+') == len(row): return flip
    return 'IMPOSSIBLE'
    

import sys

inputFile = sys.argv[1]
outFile = sys.argv[2]

fo = open(outFile, 'w')

with open(inputFile, 'r') as f:
    #print f.readline()
    t = int(f.readline())
    for i in range(t):
        r, fs = f.readline().split(' ')
        out =  "Case #{}: {}".format(i+1, flipPancakes(r,int(fs)))
        fo.write(str(out)+'\n')

fo.close()
