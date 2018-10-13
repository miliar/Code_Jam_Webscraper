import sys

def standing_ovation(shy):
	claps = 0
	diff = 0
	for i in range(len(shy)):
		if claps < i:
			diff = diff + i-claps
			claps = i
		claps = claps + shy[i]
	return diff

if __name__ == "__main__":
	f = open("A-large.in")
	output = open("A-large.out", "w")
 	cases = int(f.readline())
 	for i in range(cases):
		split = f.readline().split()
		Smax = int(split[0])
		shy = []
		for j in range(Smax+1):
			shy.append(int(split[1][j]))
		output.write("Case #" + str(i+1)+ ": " + str(standing_ovation(shy))+"\n")
	f.close()
	output.close()
  
