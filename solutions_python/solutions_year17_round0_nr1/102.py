r'''
args = ' '.join([
	r'',
])
import os
import sys
os.system(sys.executable + " %s %s"%(__file__, args))
#os.system(r'C:\Python36-32\python' + " %s %s"%(__file__, args))
r'''

input = """\
3
---+-++- 3
+++++ 4
-+-+- 4
""".splitlines(keepends=True)

#input = open(r'C:\Users\user1\Downloads\A-small-attempt0.in').readlines()
input = open(r'C:\Users\user1\Desktop\A-Large.in').readlines()
input = iter(input)

def solve(P,K):
	P = [c=='+' for c in P]
	#print(P, -K+1)
	count = 0
	for i,_ in enumerate(P[:-K+1]):
		if P[i]: continue
		count += 1
		for k in range(K):
			P[i+k] = not P[i+k]
		#print(P)
	for p in P[-K+1:]:
		if not p: return -1
	return count

caseCnt = int(next(input))
for case in range(1,caseCnt+1):
	P,K = next(input).split()
	K = int(K)
	res = solve(P,K)
	if res!=-1:
		print("Case #%d:"%case, res)
	else:
		print("Case #%d:"%case, "IMPOSSIBLE")
	
exit(0)
if __name__ == '__main__':
	import sys
	print(sys.argv)
	print(sys.executable)
	print(sys.version)
	import ctypes
	print(ctypes.sizeof(ctypes.c_size_t))

#'''
