def get_int(s):
	return int(s[:(len(s)-1)])
	
def get_list_float(s):
	s = s[:len(s)-2]
	s = s.split(' ')
	result = []
	for i in s:
		i = float(i)
		temp = "%.5f" % i
		result.append(temp)
	return result

def eval_war(naomi,ken):
	n = len(naomi)-1
	score = 0
	while n>=0:
		chosen_naomi = naomi[n]
		if chosen_naomi < ken[0]:
			chosen_ken = ken[0]
		elif chosen_naomi > ken[n]:
			chosen_ken = ken[0]
		else:
			for block in ken:
				if block > chosen_naomi:
					chosen_ken = block
					break
		if chosen_naomi > chosen_ken:
			score += 1
		naomi.remove(chosen_naomi)
		ken.remove(chosen_ken)
		n -= 1
	return score
		
def eval_dec(naomi,ken):
	n = len(naomi)-1
	score = 0
	while n>=0:
		chosen_naomi = naomi[0]
		if ken[0] < chosen_naomi:
			score+=1
			ken.remove(ken[0])
		else:
			ken.remove(ken[n])
		naomi.remove(chosen_naomi)
		n-=1
	return score
				
def process_file(filename):
	fin = open(filename,'r')
	n = get_int(fin.readline())
	for i in range(0,n):
		l = get_int(fin.readline())
		x1 = get_list_float(fin.readline())
		y1 = get_list_float(fin.readline())
		x1.sort()
		y1.sort()
		x2 = x1
		y2 = y1
		war = eval_war(x1,y1)
		#dec = eval_dec(x2,y2)
		print war
	return 0
	
if __name__ == '__main__':
	import sys
	if len(sys.argv) != 2:
		sys.stderr.write("USAGE: %s <coll-file>\n" % sys.argv[0])
		ys.exit()	
	l = process_file(sys.argv[1])