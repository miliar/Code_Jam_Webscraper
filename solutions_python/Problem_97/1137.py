
def check(i, j):
	
	istr = str(i)
	jstr = str(j)
	if len(jstr) != len(istr):
		return False
	for sz in range(len(jstr)):
		if (istr[-sz:] + istr).startswith(jstr):
			return True
	return False

def solve_slow(start, end):
	ans = 0
	for i in range(start, end+1):
		for j in range(i+1, end+1):
			if check(i, j):
				#print "%s, %s" % (i, j)
				ans += 1
	return ans

def count(i, start, end):
	istr = str(i)
	count = set()
	for sz in range(len(istr)):
		auxs = istr[-sz:] + istr[:-sz]
		aux = int(istr[-sz:] + istr[:-sz])
		if aux > i and start < aux <= end: # and not auxs.startswith("0"):
			count.add(aux)
			#if i not in count:
			#	print "%s, %s" % (i, aux)
	return len(count)

def solve_fast(start, end):
	ans = 0
	for i in range(start, end+1):
		ans += count(i, start, end)
	return ans

if __name__ == "__main__":
	ntc = int(raw_input())
	for tc in range(1,ntc+1):
		fields = raw_input().split()
		start = int(fields[0])
		end   = int(fields[1])
		#s_slow = solve_slow(start, end)
		s_fast = solve_fast(start, end)
		#assert s_slow == s_fast
		print "Case #%s: %s" % (tc, s_fast)
		



