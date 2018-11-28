import re,sys
def _scans():
	while True:
		yield from input().split()
scans = _scans().__next__
scan = lambda: int(scans())
red = lambda *a,**kw:print(*a,**kw,file=sys.stderr)

def calc(dest,horse):
	return str(dest/max((dest-init)/spd for init,spd in horse if init <= dest))

'''
if True:
	'''
sys.stdin = open('input.txt')
with open('output.txt','w') as sys.stdout:#'''
	for t in range(scan()):
		red('Case #%d'%(t+1))
		print('Case #%d: %s'%(t+1,calc(scan(),[(scan(),scan()) for i in range(scan())])))