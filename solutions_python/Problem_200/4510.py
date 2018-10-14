t = int(input())

c = 0

while c < t:

	c += 1
	
	n = input()
	aux = 0	

	if n != "".join(sorted(n)):
		for i in range(len(n)-1):

			if int(n[i]) >= int(n[i+1]):
				aux = int(n[i+1:]) + 1
				break
	
	print('Case #{}: {}'.format(c,int(n)-aux))
