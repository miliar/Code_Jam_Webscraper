from sys import argv, stdout
from os import system

def subsolve(N,K):
	if K == 1:
		return "%d %d" % (N/2, (N-1)/2)
		
	stalls_odd = N % 2 == 1
	shitters_odd = K % 2 == 1
	if stalls_odd:
		if shitters_odd:
			return subsolve((N-1)/2, (K-1)/2)
		else:
			return subsolve((N-1)/2, K/2)
	else:
		if shitters_odd:
			return subsolve((N-1)/2, (K-1)/2)
		else:
			return subsolve(N/2, K/2)

def solve(line):
	N, K = map(int, line.split(" "))
	return str(subsolve(N,K))
	
def simulate(line):
	N, K = map(int, line.split(" "))
	if (K > 300):
		return ""
	empty_seats = set(range(N))
	empty_seat_scores = {i:(0,0,0) for i in empty_seats}
	occupied_seats = set([-1, N])
	
	seat_map = ["_" for i in range(N)]
	
	chosen_score = ((N-1)/2,N/2,N/2)
	chosen_seat = N / 2
	for i in range(K):
		if len(occupied_seats):
			for seat in empty_seats:
				left_seat = max([s for s in occupied_seats if s < seat])
				right_seat = min([s for s in occupied_seats if s > seat])
				empty_seat_scores[seat] = (-min(seat - left_seat - 1, right_seat - seat - 1), -max(seat - left_seat - 1, right_seat - seat - 1), seat)
		
			chosen_seat = min(empty_seat_scores, key=empty_seat_scores.get)
			chosen_score = empty_seat_scores[chosen_seat]
		
		seat_map[chosen_seat] = "*"
		print "".join(seat_map)
		seat_map[chosen_seat] = "+"
		empty_seats.remove(chosen_seat)
		del empty_seat_scores[chosen_seat]
		occupied_seats.add(chosen_seat)
		
	return str(-chosen_score[0]) + " " + str(-chosen_score[1])

if __name__ == "__main__":
	infile = open(argv[1], 'r')
	outfile = stdout
	if len(argv) > 2:
		#pass
		outfile = open(argv[2], 'w')
	infile.readline()
	for (i,line) in enumerate(infile):
		 outfile.write(("Case #%d: " + solve(line.strip('\n'))) % (i+1) + "\n")
		 #system("pause")