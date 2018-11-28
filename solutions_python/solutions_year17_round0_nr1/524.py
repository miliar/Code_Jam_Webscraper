import re,sys
def _scans():
	while True:
		yield from input().split()
scans = _scans().__next__
scan = lambda: int(scans())
red = sys.stderr.write

sys.stdin = open('input.txt')
redir_out = 1

from collections import deque
def calc(pan,k):
	flip = 0
	pan = [i=='+' for i in pan]
	due = deque()
	state = ''
	flips = False
	for j,i in enumerate(pan):
		if due and due[0] == j:
			due.popleft()
			flips = not flips
		if flips:
			i = not i
		if not i:
			flip += 1
			flips = not flips
			due.append(j+k)
	if due and due[0] == len(pan):
		due.popleft()
	if due:
		return 'IMPOSSIBLE'
	return str(flip)


with open('output.txt','w') if redir_out else sys.stdout as sys.stdout:
	for t in range(scan()):
		red('%d\n'%t)
		print('Case #%d: %s'%(t+1,calc(scans(),scan())))