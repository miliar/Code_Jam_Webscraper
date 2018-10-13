def war(n,k):
	points = 0
	for block in n:
		if(block > max(k)):
			points+=1
			k.remove(min(k))
		else:
			for x in sorted(k):
				if(x > block):
					k.remove(x)
					break
	return points

def d_war(n,k):
	points = 0
	n = sorted(n)
	k = sorted(k)
	for i in range(len(n)):
		if(n[i] > k[i]):
			points+=1
		else:
			k.insert(0,k.pop())
	return points

f = open('war.in')
lines = f.readlines()
f.close()

num_cases = int(lines[0].strip())

curr = 1
answers = []
while (num_cases != 0):
	blocks = int(lines[curr].strip())
	naomi_raw = lines[curr+1].strip().split()
	ken_raw = lines[curr+2].strip().split()
	naomi = [float(x) for x in naomi_raw]
	ken = [float(x) for x in ken_raw]
	answers.append((d_war(naomi,ken),war(naomi,ken)))
	curr += 3	
	num_cases -= 1
#### END WHILE

case = 1
f = open('war.out','w')
for answer in answers:
	f.write("Case #{0}: {1} {2}\n".format(case,answer[0],answer[1]))
	case+=1
f.close()