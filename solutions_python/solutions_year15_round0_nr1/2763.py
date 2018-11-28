import sys

fpath = sys.argv[1]
#outfile= sys.argv[2]
f = open(fpath, 'r')

content = f.readlines()
content = [jj.strip() for jj in content]

t = int(content[0]) #no. of test cases
#out = open(outfile,'w')
def evaluate(max_shy, au, standing, frnds):
	for ii in range(max_shy+1):
		if ii == len(au):
			break
		standing = int(au[ii]) + standing
		if standing >= ii + 1:
			continue		
		else:
			addfrnds = ((ii + 1) - standing)
			frnds =  frnds + addfrnds
			standing = standing + addfrnds

	return frnds

for jj in range(1,t+1):
	inp = content[jj]
	max_shy, au = inp.split()
	max_shy = int(max_shy)
	frnds = 0
	standing = 0

	frnds = evaluate(max_shy, au, standing, frnds)
		

	print 'Case #%d: %d'%(jj,frnds)	


