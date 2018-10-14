import sys
for z in range(int(input())):
	P = sys.stdin.readline().strip('\n').split(" ")
	pancakes = P[0]
	oversize = int(P[1])
	Heads_set = set(pancakes)
	count = 0
	if(len(pancakes) == 1):
		if oversize == 1 and pancakes == '-':
			count +=1
		elif oversize > 1:
			count = "IMPOSSIBLE"
	else:
		k = pancakes.find("-")
		pancakes = list(pancakes)
		sub = list(pancakes[k:])
		while ("".join(Heads_set) != "+" and len(sub) >= oversize):
			for l in range(len(sub[:oversize])):
				if sub[l] == "+":
					sub[l] = "-";
				else:
					sub[l] ="+";
			count += 1
			pancakes[k:] = sub
			k ="".join(pancakes).find("-")
			sub = list(pancakes[k:])
			Heads_set = set(pancakes)
		if ("".join(Heads_set) != "+"):
			count = "IMPOSSIBLE"






	print("Case #{}: {}".format(z+1,count))