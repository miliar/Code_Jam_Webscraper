import itertools
input=open("in.txt","r")
output=open("out.txt","w")
n_cases=int(input.readline())
for case in range(1,n_cases+1):
	n,k=map(int, input.readline().split())
	orig=[]
	for row_n in range(n):
		orig.append([val for val in input.readline().strip()])
	#Reposition
	turned=[]
	for row in orig:
		new_row=[]
		for val in row[::-1]:
			if val!=".":
				new_row.append(val)
		new_row+=["."]*(n-len(new_row))
		turned.append(new_row)
	#Calculate
	dirs=[(0,1),(1,1),(1,0),(1,-1)]#Only need to look at half
	def in_range(row, col):
		return row>=0 and col>=0 and row<n and col<n
	win=set()
	for r0,c0 in itertools.product(range(n), range(n)):
		for dir in dirs:
			#Check if n in a row
			seen=None
			for mov in range(k):
				r=r0+mov*dir[0]
				c=c0+mov*dir[1]
				if not in_range(r,c):
					break;
				val=turned[r][c]
				if val==".":
					break
				if seen!=None and val!=seen:
					break
				seen=val
				if mov==k-1:
					#Last one!
					win.add(seen)
	#Output
	if len(win)==0:
		win_str="Neither"
	elif len(win)==2:
		win_str="Both"
	elif "R" in win:
		win_str="Red"
	elif "B" in win:
		win_str="Blue"
	output.write("Case #{0}: {1}\n".format(case, win_str))
					
	
				
	
			
		