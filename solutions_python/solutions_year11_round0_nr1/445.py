def int_input():
	return int(raw_input())

def seq_input():
	seq = []
	ch = raw_input().split()
	ch.pop(0)
	for i in range(len(ch) / 2):
		seq.append((ch[i*2], int(ch[i*2+1])))
	return seq

def solve(cid):
	seq = seq_input()
	pos_o = pos_b = 1
	time_o = time_b = 0
	for s in seq:
		if s[0] == 'O':
			time_o = max(time_o + abs(pos_o-s[1]), time_b) + 1
			pos_o = s[1]
		elif s[0] == 'B':
			time_b = max(time_b + abs(pos_b-s[1]), time_o) + 1
			pos_b = s[1]
	print 'Case #%d: %d' % (cid, max(time_o, time_b))

def main():
	for i in range(1, int_input()+1):
		solve(i)

main()

