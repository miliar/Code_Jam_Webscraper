import pdb

file = open('A-large.in', 'r')
n = int(file.readline())
for i in range(n):
    line = file.readline().strip().split(' ')
    ma = int(line[0])
    S = [int(j) for j in line[1]]
    res = [k - sum(S[0:k]) for k in range(ma+1)]
    add = max(res)
    add = max(add, 0)
    print "Case #%s: %s" % (str(i+1), str(add))
    
