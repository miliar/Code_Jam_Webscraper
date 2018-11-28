from sys import argv
def get_trains(f):
    turnaround = int(f.readline())
    As,Bs = [int(x) for x in f.readline().split()]
    i = 0
    A,B = [],[]
    def time2int(time):
        h,m = [int(x) for x in time.split(':')]
        return h*60+m
    while i<As:
        i+=1
        A.append(map(time2int,f.readline().strip().split()))
    i=0
    while i<Bs:
        i+=1
        B.append(map(time2int,f.readline().strip().split()))
    return turnaround,A,B
def neededTrains(frm,to,t_a):
	def mycmp(x,y):
		if x[0]==y[0] and x[1]==y[1]: return 0
		if x[0]<y[0]: return -1
		if x[0]>y[0]: return 1
		if x[1]<y[1]: return 1
		return -1
	frm = [(x,-1) for x in frm]
	to =  [(x+t_a,1) for x in to]
	times = (frm+to)
	times.sort(cmp=mycmp)
	sum = 0
	min_val = 0
	for t,v in times:
		sum += v
		min_val = min(min_val,sum)
	return min_val

geti = lambda x,i: map(lambda a: a[i],x)
if __name__=='__main__':
    f = open(argv[1],'r')
    out = open(argv[1]+'.out','w')
    num_lines = int(f.readline())
    cur_line = 1
    while cur_line<=num_lines:
        t_a,A,B = get_trains(f)
        A_needs = -1*neededTrains(geti(A,0),geti(B,1),t_a)
        B_needs = -1*neededTrains(geti(B,0),geti(A,1),t_a)
        out.write('Case #%d: %d %d\n' % (cur_line,A_needs,B_needs))
        print 'Case #%d: %d %d' % (cur_line,A_needs,B_needs)
        
        cur_line += 1
    out.close()
    f.close()
    