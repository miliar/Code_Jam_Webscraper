from timeit import default_timer as timer
import math

def stalls(n, k):
        l = math.floor(math.log(k, 2))
        p = k - 2**l + 1
        sum_l = n - 2**l + 1
        x = math.floor(sum_l / 2**l) + 1
        n_x = sum_l % 2**l
        x = x - int(p > n_x)

#        print l, p, x, n_x
        if x % 2 == 0:
                return int(x/2), int(x/2 -1)
        else:
                return int((x-1)/2), int((x-1)/2)

start = timer()
filename = 'C-small-2-attempt0'
f = open(filename + '.in', 'r')
g = open(filename + '.out', 'w')
t = int(f.readline())

for i in xrange(1, t+1):
	n, k = [int(j) for j in f.readline().split(' ')]
	rs, ls = stalls(n, k)
	g.write('Case #' + str(i) + ': ' + str(rs) + ' ' + str(ls) + '\n')

f.close()
g.close()
end = timer()
print (end - start)
