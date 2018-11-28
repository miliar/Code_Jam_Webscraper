import copy
import math

def rotate_list(l, offset):
    """
    Rotate a list by (offset) elements. Elements which fall off
    one side are provided again on the other side.
    Returns a rotated copy of the list. If (offset) is 0,
    returns a copy of (l).
    
    Examples:
        >>> rotate_list([1, 2, 3, 4, 5, 6], 2)
        [3, 4, 5, 6, 1, 2]
        >>> rotate_list([1, 2, 3, 4, 5, 6], -2)
        [5, 6, 1, 2, 3, 4]
    """
    if len(l) == 0:
        raise ValueError("Must provide a list with 1 or more elements")
    if offset == 0:
        rv = copy.copy(l)
    else:
        real_offset = offset % int(math.copysign(len(l), offset))
        rv = (l[real_offset:] + l[:real_offset])
    return rv


T = int(raw_input().strip())

for i in range(T):
	Rt,kt,Nt = (raw_input().strip()).split(' ')
	R = int(Rt)
	k = int(kt)
	N = int(Nt)
	
	#print ''
	#print '~Rounds:', R
	#print '~Max People:', k
	#print '~Groups:', N

	g = []
	gt = (raw_input().strip()).split(' ')
	for j in range(len(gt)):
		g.append(int(gt[j]))

	#print g
	#print ''
	#print p
	#p = rotate_list(g, 3)

	money=0

	for j in range(R):
		#print 'Round:', j
		sum=0
		for x in range(len(g)):
			if((sum + g[0]) <= k):
				sum = sum + g[0]
				#print 'Allowed group:', g[0]
				#print 'Money so far:', sum
				g = rotate_list(g, 1)
				#print g
			else:
				break
		money = money + sum
 		#print '---Money this round:', money
	#print '!!!Total Money:', money
			
		
	output = 'Case #' + repr(i+1) + ': ' + repr(money)
	print output
