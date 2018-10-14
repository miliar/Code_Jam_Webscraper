
def main(fn=''):
	if fn == '':
		fn = raw_input('File name: ')
	fin = open(fn)
	o = open('output.txt','w')
	no_iter = int(fin.readline())
	for x in xrange(no_iter):
		para = fin.readline().split(' ')
		ls = []
		for i in range(int(para[0])):
			ls.append(int(para[3+i]))
		o.write("Case #"+str(x+1) + ": " + str(j2(int(para[1]),int(para[2]),ls)) + '\n')
	fin.close()
	o.close()

def ml(n , target):
	temp = []
	potential = 1
	aver = n/3
	if n % 3 == 2:
		aver += 1
	
	for j in range(2):
		temp.append(aver)
	temp.append(n - 2*aver)
	score = max(temp)
	if n % 3 == 1 or target - score != 1 or n == 0:
		potential = 0

	return score, potential

def j2(max_surprise,required,ls):

	more_or_equal = []
	one_less_with_potential = []

	for i in ls:
		scr , pot = ml(i , required)
		if scr > required -1:
			more_or_equal.append(scr)
		elif scr == required -1 and pot:
			one_less_with_potential.append(scr)

	
	counts = len(more_or_equal)

	if len(one_less_with_potential) >= max_surprise:
		counts += max_surprise
	else:
		counts += len(one_less_with_potential)
	print required,max_surprise,counts ,more_or_equal, one_less_with_potential

	return counts

main(fn ='')