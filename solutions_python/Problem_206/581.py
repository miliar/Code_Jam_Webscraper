infile = 'A-large.in'
outfile = 'al.out'
import pdb
from collections import defaultdict

def main():
	with open(infile) as f, open(outfile, 'w+') as out:
		T = int(f.readline())
		for c in range(0, T):
			print()
			print(c)
			D, N = map(int, f.readline().split(" "))
			horses = []
			for hs in range(0, N):
				K, S = map(int, f.readline().split(" "))
				horses.append((K, S))
			speed = getspeed(D, N, horses)
			out.write('Case #{0}: {1}\n'.format(c+1, speed))
			
def getspeed(d, n, horses):
	most_time_left = 0
	for i, horse in enumerate(horses):
		togo = d - horse[0]
		timeleft = float(togo) / float(horse[1])
		print(timeleft)
		if timeleft > most_time_left:
			most_time_left = timeleft
	
	speed = float(d) / most_time_left
	return speed

if __name__=='__main__':
	main()

