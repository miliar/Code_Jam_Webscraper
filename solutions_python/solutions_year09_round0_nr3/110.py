
# python 3.0



target = "welcome to code jam"



N = int(input())

for i in range(1,N+1):
	print("Case #"+str(i)+": ", end='')
	
	L = len(target)
	counts = [0 for c in target]
	counts += [0]	# one on the end for finished string
	counts[0] = 1
	
	line = input()
	for c in line:
		for j in range(len(target)):
			if c==target[j]:
				counts[j+1] += counts[j]
				counts[j+1] = counts[j+1] % 10000
	
	
	print(str(counts[L]+10000)[-4:])
	




















