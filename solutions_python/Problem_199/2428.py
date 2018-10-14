# 3
# ---+-++- 3
# +++++ 4
# -+-+- 4

# for t in range(100):
# 	print "-+"*500,1000
# '''
def flip(v):
	if v == "+":
		return "-"
	else:
		return "+"

t = input()
for i in range(t):
	s,k = raw_input().split(" ")
	s = [x for x in s]
	k = int(k)
	current_state = 0
	current_pos = 0
	flips = 0
	impossible = False
	for idx,val in enumerate(s):
		if((len(s)-idx)-k < 0):
			break
		if val == "-":
			flips +=1
			for tampered_idx in range(idx,idx+k):
				s[tampered_idx] = flip(s[tampered_idx])
	for val in s[-k:]:
		if val == "-":
			impossible = True
	if impossible:
		print "Case #%d: IMPOSSIBLE" %(i+1)
	else:
		print "Case #%d: %d" %(i+1,flips)
# '''