import sys
from collections import *

def solve(N,R,O,Y,G,B,V):
	#small: only need R,Y,B
	out = ""
	last = None
	while R>=0 and Y>=0 and B>=0 and R+Y+B>0:
		n,c = max({(R,"R"),(Y,"Y"),(B,"B")} - {last})
		last = (n-1,c)
		out += c
		if c == "R":
			R -= 1
		elif c == "B":
			B -= 1
		elif c == "Y":
			Y -= 1
	if R>0 or Y>0 or B>0:
		return "IMPOSSIBLE"
	else:
		if out[0] == out[-1]:
			wrong = out[-1]
			out = out[:-1]
			for i in range(1, len(out)):
				if out[i] != wrong and out[i-1] != wrong:
					out = out[:i] + wrong + out[i:]
					break
			else:
				return "IMPOSSIBLE"
		return out
		

T = int(input())
for case in range(T):
	colors = list(map(int, input().split()))
	print("Case #{}: {}".format(case+1, solve(*colors)))