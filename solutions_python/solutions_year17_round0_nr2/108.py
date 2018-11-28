r'''
args = ' '.join([
	r'',
])
import os
import sys
os.system(sys.executable + " %s %s"%(__file__, args))
#os.system(r'C:\Python36-32\python' + " %s %s"%(__file__, args))
r'''

import sys
input = """\
4
132
1000
7
111111111111111110
""".splitlines(keepends=True)
output = sys.stdout

if 1:
	input = open(r'C:\Users\user1\Desktop\B-small-attempt0.in').readlines()
	input = open(r'C:\Users\user1\Desktop\B-Large.in').readlines()
	output = open(r'C:\Users\user1\Desktop\B.out', "w")
	
input = iter(input)

def solve(N):
	N = [int(n) for n in N]
	
	top = 0
	for i in range(len(N)-1):
		if N[i]>N[i+1]:
			break
		if N[i] != N[i+1]:
			top = i+1
	else:
		return ''.join(map(str,N))
	
	for j in range(top+1,len(N)):
		N[j] = 9
	
	N[top] -= 1
	return ''.join(map(str,N)).strip('0')
	
	#for i,_ in enumerate(N[:-1]):
	
caseCnt = int(next(input))
for case in range(1,caseCnt+1):
	N = next(input).strip()
	res = solve(N)
	if res!=-1:
		print("Case #%d:"%case, res, file=output)
	else:
		print("Case #%d:"%case, "IMPOSSIBLE", file=output)
	
#'''
