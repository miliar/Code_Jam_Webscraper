def fair(naomi, ken):
	kh = 0
	kt = len(ken)-1
	point = 0
	for i in range(-1,-len(naomi)-1,-1):
		if ken[kt] > naomi[i]:
			kt = kt - 1
		else:
			kh = kh + 1
			point = point + 1
	return point

def deceive(naomi, ken):
	ni = 0
	point = 0
	for block in ken:
		if ni < len(naomi):
			while naomi[ni] < block:
				ni = ni + 1
				if ni >= len(naomi):
					break
			if ni >= len(naomi):
				break
			else:
				ni = ni + 1
				point = point+1
		else:
			break
	return point

def solve():
	ntest = int(raw_input())
	for t in range(0,ntest):
		N = int(raw_input())
		tmp = raw_input().split(" ")
		naomi = []
		for ele in tmp:
			naomi.append(float(ele))
		naomi.sort()
		tmp = raw_input().split(" ")
		ken = []
		for ele in tmp:
			ken.append(float(ele))
		ken.sort()
		point_dece = deceive(naomi, ken)
		point_fair = fair(naomi, ken)		
		print "Case #%d: %d %d" % (t+1, point_dece, point_fair)
		

if __name__ == "__main__":
	solve()
