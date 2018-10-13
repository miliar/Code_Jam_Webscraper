from collections import Counter
t = int(input(''))
c = 0
while True:
	t-=1
	if t < 0:
		break
	c += 1
	
	res = []
	
	n = int(input(''))
	row = 4
	for i in range(row):
		inp = input('')
		if i+1 == n:
			res.extend([int(p, 10) for p in inp.split(' ')])
			
	
	n = int(input(''))
	row = 4
	for i in range(row):
		inp = input('')
		if i+1 == n:
			res.extend([int(p, 10) for p in inp.split(' ')])
			
	s = set(res)
	
	if len(s) == 7:
		ret = [k for k,v in Counter(res).items() if v>1]
		print("Case #"+ str(c) +":", ret[0])
	elif len(s) == 8:
		print("Case #"+ str(c) +": Volunteer cheated!")
	elif len(s) < 7:
		print("Case #"+ str(c) +": Bad magician!")
