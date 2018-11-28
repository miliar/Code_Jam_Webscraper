import sys

filename = 'B-large.in'
input_filename=open(filename)
with input_filename as f:
    content = f.readlines()
content = [x.strip() for x in content] 


'''T = raw_input().strip()
T = int(T)
N = []
for a0 in range(T):
	n = raw_input().strip()
	N.append(n)'''

T = int(content[0])
N = content[1:]
	
#print N, N[-1][-2:]

for i in range(T):
	#print "i",i
	n = []
	l = len(N[i])
	if(len(N[i])>1):
		t = 0
		for j in range(len(N[i])-1):
			#print "j",j
			if(int(N[i][j])==int(N[i][j+1])):
				t= j+1
				#print N[i][j],j
			if(int(N[i][j])>int(N[i][j+1])):
				N[i] = N[i][:j]+str((int(N[i][j])-1)%10)+'9'*(l-j-1)
				#print N[i]
				break

		for j in range(t,0,-1):
			#print "j",j,N[i][j]
			if(int(N[i][j])<int(N[i][j-1])):
				N[i] = N[i][:j-1]+str((int(N[i][j-1])-1)%10)+'9'*(l-j)
				#print N[i]

		if(int(N[i][0])>int(N[i][1])):
			N[i] = str((int(N[i][0])-1))+'9'*(l-1)
			#print N[i]


		N[i] = str(int(N[i]))
	####################################################################################################


print N
output_filename=open('op.txt','w')
for i in range(len(N)):
	#print 'Case #'+str(i+1)+': '+str(N[i])
	output_filename.write('Case #'+str(i+1)+': '+str(N[i]))
	output_filename.write('\n')
output_filename.close()