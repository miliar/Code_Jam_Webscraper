from sys import exit
T = int(raw_input())

for i in range(T):
	a1 = int(raw_input())
	m1 = [[int(k) for k in raw_input().split()] for j in range(4)][a1-1]
	a2 = int(raw_input())
	m2 = [[int(k) for k in raw_input().split()] for j in range(4)][a2-1]
	
	m = [val for val in m1 if val in m2]

	if len(m) == 1:
		result = str(m[0])
	elif len(m) > 1:
		result = "Bad magician!"
	else:
		result = "Volunteer cheated!"

	print("Case #"+str(i+1)+": "+result)
