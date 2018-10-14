f = file("input-large.in")
g = file("output.txt", "w")

lines = f.read().split('\n')

out = [x for x in lines if lines.index(x) % 3 != 1]

length = out.pop(0)

def fairPlay(out):
	naomi = set(out[2*n].split())
	ken = sorted(out[2*n + 1].split())
	
	score = 0
	
	while naomi:
	
		nChoice = naomi.pop()
		kChoices = filter(lambda x: x > nChoice, ken)
	
		if kChoices:
			ken.remove(kChoices[0])
	
		else: 
			ken.pop(0)
			score += 1

	return score

def haxPlay(out):
	naomi = sorted(out[2*n].split())
	ken = sorted(out[2*n + 1].split())

	score = 0
	
	while naomi:

		if naomi[-1] > ken[-1]:
			naomi.pop()
			ken.pop()
			score += 1

		else:
	
			nChoice = naomi.pop(0)

			if nChoice < ken[-1]:
				ken.pop()
			else:
				ken.pop(0)
				score += 1

	return score

for n in range(int(length)):
	haxScore = haxPlay(out)
	score = fairPlay(out)
	
	g.write("Case #" + str(n+1) + ": " + str(haxScore) + " " + str(score)+"\n")

g.close()