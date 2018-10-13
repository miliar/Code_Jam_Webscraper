def isRecycled(n, m):
	for i in range(len(n)):
		if n[i:len(n)]+n[0:i] == m:
			return True
	return False

f = open("input.in", "r")
out = open("output", "w")

T = int(f.readline())
for i in range(T):
	cont = 0
	input = f.readline()
	input = input.split()
	A = int(input[0])
	B = int(input[1])
	n = A
	m = B+1
	for n in range(A, m):
		for m in range(n, B+1):
			if n<m:
				if isRecycled(str(n), str(m)):
					cont += 1
	out.write('Case #'+str(i+1)+': '+str(cont)+'\n')
	print cont
out.close()
f.close()
				