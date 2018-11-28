#!/usr/bin/python




def main():
	a = open("input.txt","r")
	num_lines = int(a.readline())
	
	for k in range(num_lines):
		line = a.readline().split()
		scores = []
		n = int(line[0])
		s = int(line[1])
		p = int(line[2])
		for j in range(3,n+3):
			scores.append(int(line[j]))

		most = 0
		scores.sort(reverse=True)
		stop = 0
		for i in range(len(scores)):
			if scores[i]/3.0 > p - 0.667:
				most += 1
				stop = i+1

		if s:
			for i in range(stop,min(len(scores),s+stop)):
				if p > 1:
					if scores[i]/3.0 > p - 1.34:
						most += 1
				else:
					if scores[i] > p:
						most += 1

		print "Case #" + str(k+1) + ": " + str(most)


if __name__ == "__main__":
	main()
