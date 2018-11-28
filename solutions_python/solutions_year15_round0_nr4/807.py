import sys

def omino(X,R,C):
	if (R*C % X) != 0:
		return "RICHARD"
	if (R < X/2) or (C < X/2):
		return "RICHARD"
	if (R == X/2) or (C == X/2):
		T = R
		if (R == X/2):
			T = C
		for c in range(X/2):
			d = X/2-c
			win = 1
			for a in range(T):
				b = T-1-a
				if (b >= d) and (a >= c):
					if (((a-c) % X) == 0) and (((b-d) % X) == 0):
						win = 0
			if win == 1:
				return "RICHARD"	
	if X >= 7:
		return "RICHARD"
	return "GABRIEL"

if __name__ == "__main__":
	input = "D-small-attempt2"
	f = open(input + ".in")
	output = open(input + ".out", "w")
 	cases = int(f.readline())
 	for i in range(cases):
		split = f.readline().split()
		X = int(split[0])
		R = int(split[1])
		C = int(split[2])		
		output.write("Case #" + str(i+1)+ ": " + str(omino(X,R,C))+"\n")
	f.close()
	output.close()
  
