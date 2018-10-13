nums = []

for i in xrange(1,100000000):
    if str(i) == str(i)[::-1] and str(i*i) == str(i*i)[::-1]:
        nums.append(i*i)
f = open('in.txt')
N = int(f.readline())
for i in xrange(N):
    a,b = map(int, f.readline().split())
    filtered = [x for x in nums if x >= a and x <= b]
    print 'Case #%d: %d' % (i+1, len(filtered))