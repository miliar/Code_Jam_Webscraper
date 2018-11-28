out = open('B-out-large.txt', 'w')

def convTime(time):
    a = time.split(':')
    return int(a[0])*60+int(a[1])
    

def read(filename):
    f = open(filename)
    
    cases = int(f.readline())
    
    for i in range(cases):
	turnaround = int(f.readline())
	
	nextline = f.readline()
	
	numbers = nextline.split(' ')
	na = int(numbers[0])
	nb = int(numbers[1])
	
	A_departures = []
	B_arrivals = []
	for j in range(na):
	    nextline = f.readline()
	    
	    times = nextline.split(' ')
	    
	    A_departures.append(convTime(times[0]))
	    B_arrivals.append(convTime(times[1]))
	
	B_departures = []
	A_arrivals = []
	for j in range(nb):
	    nextline = f.readline()
	    
	    times = nextline.split(' ')
	    
	    B_departures.append(convTime(times[0]))
	    A_arrivals.append(convTime(times[1]))
	    
	ans1, ans2 = compute(turnaround, A_departures, B_arrivals, B_departures, A_arrivals, na, nb)
	
	out.write("Case #%d: %d %d\n" % (i+1, ans1, ans2))

    f.close()
	
	
def compute(turnaround, A_departures, B_arrivals, B_departures, A_arrivals, na, nb):
    
    
    availableAtB = []
    
    for i in B_arrivals:
	availableAtB.append(i+turnaround)
	
    availableAtA = []
    for i in A_arrivals:
	availableAtA.append(i+turnaround)
	
    
    availableAtB.sort()
    availableAtA.sort()
    B_departures.sort()
    A_departures.sort()
    
    i=0
    j=0
    
    while i<len(availableAtB) and j<len(B_departures):
	print i, j, availableAtB[i], B_departures[j]
	if availableAtB[i] <= B_departures[j]:
	    print "found one at B"
	    nb -= 1
	    i += 1
	    j += 1
	else:
	    j += 1
	    
    i=0
    j=0
    
    while i<len(availableAtA) and j<len(A_departures):
	print i, j, availableAtA[i], A_departures[j]
	if availableAtA[i] <= A_departures[j]:
	    print "found one at A"
	    na -= 1
	    i += 1
	    j += 1
	else:
	    j += 1
	    
    return na, nb
    
read('B-large.in')
out.close()