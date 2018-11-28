import math
n_cases=raw_input()

for t in range(int(n_cases)):
	pancakes=[]
	input_string=raw_input().split()
	n=int(input_string[0])
	k=int(input_string[1])

	for line in range(n):
		s=raw_input().split()
		pancakes+=[ (int(s[0]),int(s[1])) ]

	pancakes.sort(key=lambda x: -x[1]*x[0])

	best_area=0
	for i in range(len(pancakes)):
		area=pancakes[i][0]*pancakes[i][0]
		area+=(2*pancakes[i][0]*pancakes[i][1])
		base_radius=pancakes[i][0]
		n_pancakes=1

		for j in range(len(pancakes)):
			if n_pancakes==k:
				break
			elif pancakes[j][0]<=base_radius and i!=j:
					area+=(2*pancakes[j][0]*pancakes[j][1])
					n_pancakes+=1
		
		if area>best_area:
			best_area=area

	print('Case #%d: %f' % (t+1, best_area*math.pi))
