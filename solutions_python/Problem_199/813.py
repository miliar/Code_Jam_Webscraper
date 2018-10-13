import sys

T = int(raw_input())

for t in range(1, T+1):
    S,K = raw_input().split()
    K = int(K)
    S = list(S)

    num = 0

    for i in range(len(S) - K + 1):
    	if S[i] == '-':
    		for j in range(i, i+K):
    			S[j] = '+' if S[j] == '-' else '-'
    		num += 1
    	#print i, ''.join(S)

    if '-' in S:
    	print 'Case #%d: IMPOSSIBLE' % (t)
    else:
	    print 'Case #%d: %d' % (t, num)
