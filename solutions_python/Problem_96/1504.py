def solve(N, S, p, scores):
	count = 0
	for s in scores:
		d = s%3 
		c = s / 3
		if d <= 1 and c + d >= p:
			count += 1
			continue
		if d == 2 and c+1 >= p:
			count +=1
			continue
		if d == 0 and s > 2 and c+1 >=p and S > 0:
			count += 1
			S -= 1
			continue
		if d ==2 and c + 2 >= p and S > 0:
			count += 1
			S -= 1
			continue
			
	return count			

def main():
	T = int(raw_input())
	for i in range(T):
		ints = [int(x) for x in raw_input().split(" ")]
		N = ints[0]
		S = ints[1]
		p = ints[2]
		scores = ints[3:][:N]
		print "Case #%d: %d"%(i+1, solve(N,S,p,scores))
		
main()