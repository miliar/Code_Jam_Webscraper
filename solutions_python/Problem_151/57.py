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

def check(sv,svn):
	global mcount
	if not all(i!=1 for i in svn):
		return
	ss= sum(svn)
	if( ss>mcount[0]):
		mcount =ss,1
	elif ss==mcount[0]:
		mcount = ss,mcount[1]+1
	# print(sv)
	# print(svn)

def addx(arr,val):
	count =0
	for i in arr:
		for j in range(min(len(val),len(i))):
			if val[j] == i[j]:
				count = max(count,j+1)
			else:
				break
	return len(val)-count

def rec(depth,osv,osvn):
	if(depth < 0):
		return check(osv,osvn)
	for i in range(m):
		# sv = [ix[:] for ix in osv]
		# svn = osvn[:]
		dd=addx(osv[i],inp[depth])
		osvn[i] += dd
		osv[i] += [inp[depth]]
		rec(depth-1,osv,osvn)
		osvn[i] -= dd
		osv[i].pop()

for testcase in range(scan()):
	n,m = scan(),scan()
	sv = [[] for i in range(m)]
	svn = [1]*m
	mcount = (0,0)
	inp = [scanstr() for i in range(n)]
	rec(n-1,sv,svn)
	print('Case #%d: %d %d' %(testcase+1,mcount[0],mcount[1]))