import sys


T = raw_input().strip()
T = int(T)

S = []
for a0 in xrange(T):
	K = []
	D,N = raw_input().strip().split(' ')
	D,N = [float(D),int(N)]
	for i in range(N):
		s = raw_input().strip().split(' ')
		K.append((D - float(s[0]))/float(s[1]))
	print "k", max(K)
	S.append(str("%6f"%float(D/max(K))))
	print "ans", "%6f"%float(D/max(K))

output_filename=open('op.txt','w')

for i in range(T):
	#print 'Case #'+str(i+1)+': '+str(N[i])
	print 'Case #' +str(i+1)+': '+str(S[i])
	output_filename.write('Case #'+str(i+1)+': '+str(S[i]))
	output_filename.write('\n')
output_filename.close()