import time

def main():
	n = input()
	f = open('output.txt','w')
	for i in range(n):
		text=raw_input()
		stall=int(text.split(' ')[0])
		people=int(text.split(' ')[1])
		space=[]
		space.append((stall,1))
		nex=space[0];
		l=0;
		r=0;
		prevnum=-1
		for j in range(people):
			if nex[0]!=prevnum:
				l=int(nex[0]/2)-1+nex[0]%2
				r=int(nex[0]/2)
			if nex[1]==1:
				space.remove(nex)
			else:
				nex[1]-=1
			if(exist(r,space)==0):
				if (r!=0):
					space.append([r,1])
			else:
				tmp=[item for item in space if item[0]==r]
				tmp[0][1]+=1
			if(exist(l,space)==0):
				if l!=0:
					space.append([l,1])
			else:
				tmp=[item for item in space if item[0]==l]
				tmp[0][1]+=1
			space.sort(key=lambda tup:tup[0],reverse=True);
			if(len(space)>0):
				nex=space[0];

			if j==people-1:
				f.write("Case #{}: {} {}\n".format(i+1,r,l))
				#print("Case #{}: {} {}\n".format(i+1,r,l))
	f.close();

def exist(num,arr):
	return len([item for item in arr if item[0]==num])


if __name__ == "__main__":

	main()
