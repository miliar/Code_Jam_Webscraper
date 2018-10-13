def dostuff(A, B, K):
    c = 0
    for i in range(A):
	for j in range(B):
	    if (i & j) < K:
		c += 1
    return c

f = open('input.in')
fw = open('output.out', 'w')
g = f.readline()
g = f.readline()
case = 1
while g != "":
    arr = []
    arr=(g.replace('\n', '').split(' '))
    print arr
    m = dostuff(int(arr[0]), int(arr[1]), int(arr[2]))
    print 'Case #' + str(case) + ': ' + str(m) + '\n',
    fw.write('Case #' + str(case) + ': ' + str(m) + '\n')
    case += 1
    g = f.readline()
