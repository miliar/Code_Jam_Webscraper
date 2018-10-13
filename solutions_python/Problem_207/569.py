## 
def place(N,colors):
	ans = [None]*N
	names = ['R','O','Y','G','B','V']
	index = [i[0] for i in sorted(enumerate(colors), reverse=True, key=lambda x:x[1])]
	maxcolor = colors[index[0]]
	if maxcolor > N/2:
	 	ans = 'IMPOSSIBLE'
	else:
	 	n1 = colors[index[0]]
	 	n2 = colors[index[1]]
	 	n3 = colors[index[2]]
	 	c1 = names[index[0]]
	 	c2 = names[index[1]]
	 	c3 = names[index[2]]

	 	triples = n2 + n3 - n1
	 	doubles = n2 - triples
	 	for i in range(triples):
	 		ans[3*i] = c1
	 		ans[3*i+1] = c2
	 		ans[3*i+2] = c3
	 	for i in range(n2-triples):
	 	 	ans[3*triples+2*i] = c1
	 	 	ans[3*triples+2*i+1] = c2
	 	for i in range(n3-triples):
	 	  	ans[3*triples+2*doubles+2*i] = c1
	 	  	ans[3*triples+2*doubles+2*i+1] = c3
		ans = ''.join(ans)
	return ans

print place(6,[2,0,2,0,2,0])
print place(3,[1,0,2,0,0,0])
print place(7,[3,0,1,0,3,0])


## I/O Handler
fIn = open('B_0.txt', 'r')
fOut = open('B_0_sol.txt','w+')
nCases = int(fIn.readline())
for i in range(nCases):
	t = fIn.readline()
 	N,R,O,Y,G,B,V = t.split(" ")
 	N = int(N)
 	colors = [int(R),int(O),int(Y),int(G),int(B),int(V)]
 	ans = place(N,colors)
 	output = "Case #{}: {}\n".format(i+1,ans)
 	fOut.write(output)
fIn.close
fOut.close


