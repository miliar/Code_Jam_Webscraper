cases = [ [0,1,2,3], [4,5,6,7],[8,9,10,11],[12,13,14,15],[0,4,8,12],[1,5,9,13],[2,6,10,14],[3,7,11,15],[0,5,10,15],[3,6,9,12]]
def check_and(s, lst, x1, t_pos):
	for p in lst:
		if s[p] != x1 and p !=t_pos:
			return False;
	return True


def check_or(s, lst, x1):
	for p in lst:
		if s[p] == x1:
			return True;
	return False

def parse():
	s = ''
	s += raw_input()+raw_input()+raw_input()+raw_input()
	return s
def main():
	T = int(raw_input())
	for i in range(T):
		done = False
		if i > 0:
			raw_input()
		s = parse()
		t_pos =  s.index('T') if 'T' in s else -1
		if s.count('X') == s.count('O') :
			for c in cases:
				if check_and(s, c, 'O', t_pos):
					done = True
					print 'Case #%d: O won'	% (i+1)
					break
		else:
			for c in cases:
				if check_and(s, c, 'X', t_pos):
					done = True
					print 'Case #%d: X won'	% (i+1)
					break
		if done:
			continue
		if check_or(s, range(16), '.'):
			print 'Case #%d: Game has not completed'	% (i+1)
		else:
			print 'Case #%d: Draw' % (i+1)

if __name__=="__main__":
	main()
