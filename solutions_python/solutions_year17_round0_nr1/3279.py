def flip(cakes, i, K):
    before = cakes[:i]
    here = cakes[i:i+K]
    after = cakes[i+K:]
    here = here.replace('-','*').replace('+','-').replace('*','+')
    return before + here + after
    
def cook(cakes, K, flips,flipped):
#     print cakes, flips, flipped
    if '-' not in cakes:
#         print flipped
        return flips
    
    minimal = 10000000000
    for i in xrange(0,len(cakes)-K+1):
        if i not in flipped:
            res = cook(flip(cakes,i,K), K, flips+1,flipped+[i])
            if res!='IMPOSSIBLE':
                minimal = min(minimal,res)
    
    if minimal!=10000000000:
        return minimal
    return 'IMPOSSIBLE'

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	cakes, K = raw_input().split()
	K = int(K)
	
	print 'Case #'+str(i)+': ', cook(cakes, K, 0, [])