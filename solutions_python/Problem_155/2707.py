import time
start = time.time()
with open('A-large.in') as f:
    data = f.read().splitlines()[-1:0:-1]
ind = 0
while data:
    ind += 1
    case = data.pop().split()
    rsum, add = 0, 0
    for i in xrange(len(case[1])):
        rsum += int(case[1][i])
        if rsum < i + 1:
            add += i + 1 - rsum
            rsum += i + 1 - rsum
    print "Case #" + str(ind) + ": " + str(add)
print time.time() - start
        
