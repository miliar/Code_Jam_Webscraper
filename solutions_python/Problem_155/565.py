with open('A-large.in') as f:
	with open('A-large.out','w') as of: 
		n = int(f.readline())
		for j in range(n):
			inp = f.readline().split(" ")
			m = int(inp[0])
			audience = {}
			for i in range(m + 1):
				audience[i] = int(inp[1][i])
			added = 0
			sofar = 0
			for i in range(m + 1):
				if sofar < i:
					added += 1
					sofar += 1
				sofar += audience[i]
			of.write("Case #{}: {}\n".format(j+1,added))