for t in range(0, int(input())):
	shy, audience = input().split()
	shy = int(shy)
	audience = [int(x) for x in list(audience)]

	qtd = 0
	needed = 0
	for i in range(0, len(audience)):
		if(audience[i] > 0):
			if(i > qtd):
				needed += i - qtd
				qtd += (i - qtd)
			qtd += audience[i]
		if qtd >= shy:
			break
	print("Case #%d: %d" %(t + 1, needed))