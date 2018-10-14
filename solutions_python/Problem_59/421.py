T = int(raw_input())
fileobj = open("1_op.txt","w")
for t in range(1,T+1):
	inp = raw_input().split(' ')
	N = int(inp[0])
	M = int(inp[1])

	e_dir = []
	n_dir=""
	total_mkdir=0

	for i in range(N):
		e_dir.append(raw_input())
	for i in range(M):
		#n_dir.append(raw_input())
		n_dir = raw_input()
		
		if n_dir not in e_dir:
			total_mkdir = total_mkdir+1
			e_dir.append(n_dir)
			split_dir = n_dir.split('/')
			split_dir.pop(0)
			for x in range(len(split_dir)-1,0,-1):
				temp=""
				temp= '/' + '/'.join(split_dir[0:x])
				if temp not in e_dir:
					total_mkdir = total_mkdir+1
					e_dir.append(temp)
				else:
					break

	fileobj.write( "Case #"+str(t)+": "+str(total_mkdir)+"\n")
fileobj.close()
	