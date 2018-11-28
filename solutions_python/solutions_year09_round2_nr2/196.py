import sys;
def main():
	filename = sys.argv[1]
	f=open(filename,'r')
	outf=open("output.txt", 'w')
	tcCount=int(f.readline())
	
	for i in range(tcCount):
		#print "testcase"
		num = int(f.readline())
		numb = num
		# separate out digits
		digits = []
		while num > 0:
			digit = num %10
			num = num/10
			digits.append(str(digit))
		#generate all permutations
		digits.append('0')
		permlist = []
		for p in all_perms(digits):
			c = ''
			for k in p:
				c = c+k
			permlist.append(int(c))
		permlist = remove_dup(permlist)
		permlist.sort()
		#print permlist
		pos = permlist.index(numb)
		res = permlist[pos+1]
		outline = 'Case #'+str(i+1)+': '+str(res)
		print outline
		outf.write(outline+'\n');
		
	f.close()
	outf.close()

def remove_dup(l):
	newl=[]
	for n in l:
		if n in newl:
			pass
		else:
			newl.append(n)
	return newl
def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

	
main()
