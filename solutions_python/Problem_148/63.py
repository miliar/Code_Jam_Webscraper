import sys

buf=[]
def scanstr():
    global buf
    while not len(buf):
        buf = input().replace('\n',' ').split(' ')
    return buf.pop(0)

def scan():
    return int(scanstr())

sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

for testcase in range(scan()):
	n,cap = scan(),scan()
	inp = [scan() for i in range(n)]
	count = 0
	while len(inp):
		ii = inp.pop(0)
		jj = (-1,-1)
		for k,i in enumerate(inp):
			if ii+i <= cap and i >= jj[1]:
				jj = (k,i)
		if jj[0] != -1:
			inp.pop(jj[0])
		count += 1
	print('Case #%d: %d' %(testcase+1,count))