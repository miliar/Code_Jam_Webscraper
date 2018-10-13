t = int(input())
for i in range(1, t + 1):
	print ("Case #", i, ": ", sep ='', end='')
	s = set(range(1, 17))
	for i in range(2):
		r = int(input())
		
		x = [set(int(i) for i in input().split()) for x in range(4)]
		s &= x[r - 1]
	

	if len(s) == 1:
		print(list(s)[0])
	elif len(s) == 0:
		print("Volunteer cheated!")
	else:
		print("Bad magician!")
		
