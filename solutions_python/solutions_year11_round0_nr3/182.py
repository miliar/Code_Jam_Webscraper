def to_binary(n):
    s = ''
    while n > 0:
	if n % 2:
	    s += '1'
	else:
	    s += '0'
	n /= 2
    return s

def parse_param():
    raw_input()
    return map(int , raw_input().split())

def solve(l_):
    l = map(to_binary, l_)
    max_len = 0
    for i in l:
	max_len = max(len(i), max_len)
    for j in range(max_len):
	sum_ = 0
	for i in l:
	    try:
		sum_ += int(i[j])
	    except IndexError:
		pass
	if sum_ % 2 != 0:
	    return "NO"
    l_.sort()
    l_.pop(0)
    return sum(l_)

def main():
    T = int(raw_input())
    for i in range(1, T + 1):
	print "Case #%d:" % i,
	l = parse_param()
	print solve(l)

main()

