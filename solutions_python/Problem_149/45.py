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

def check(arr):
	st = 0
	ol = None
	for i in arr:
		if st == 0:
			st = 1
		elif st == 1:
			if i <= ol:
				st = 2
		elif st == 2:
			if i>= ol:
				return False
		ol = i
	return True

for testcase in range(scan()):
	n = scan()
	oinp = [scan() for i in range(n)]
	count = 0
	s,d = 0,n
	while not check(oinp):
		target = min((i,k+s) for k,i in enumerate(oinp[s:d]))[1]
		# print(oinp)
		# print(s,d,target)
		if(target-s < d-1-target):
			count += target-s
			oinp = oinp[:s] + [oinp[target]] + oinp[s:target] + oinp[target+1:]
			s += 1
		else:
			count += d-1-target
			oinp = oinp[:target] + oinp[target+1:d] + [oinp[target]] + oinp[d:]
			d -= 1
	print('Case #%d: %d' %(testcase+1,count))