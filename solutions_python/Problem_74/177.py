def parse_param():
    line = raw_input().split()
    N = int(line[0])
    B = []
    O = []
    turn = []
    for i in range(N):
	turn.append(line[i * 2 + 1])
	if line[i * 2 + 1] == 'B':
	    B.append(int(line[i * 2 + 2]))
	else:
	    O.append(int(line[i * 2 + 2]))
    B.append(0)
    O.append(0)
    return B, O, turn

def go_next(pos, next):
    if next == 0:
	return pos
    elif pos < next:
	return pos + 1
    elif pos > next:
	return pos - 1
    else:
	return pos

def solve(B, O, turns):
    b_pos = 1
    o_pos = 1
    b_next = B.pop(0)
    o_next = O.pop(0)
    count = 0
    for turn in turns:
	if turn == 'B':
	    while b_pos != b_next:
		b_pos = go_next(b_pos, b_next)
		o_pos = go_next(o_pos, o_next)
		count += 1
	    o_pos = go_next(o_pos, o_next)
	    count += 1
	    b_next = B.pop(0)
	else:
	    while o_pos != o_next:
		b_pos = go_next(b_pos, b_next)
		o_pos = go_next(o_pos, o_next)
		count += 1
	    b_pos = go_next(b_pos, b_next)
	    count += 1
	    o_next = O.pop(0)
    return count

def main():
    T = int(raw_input())
    for i in range(1, T + 1):
	print "Case #%d:" % i,
	B, O, turn = parse_param()
	print solve(B, O, turn)

main()
