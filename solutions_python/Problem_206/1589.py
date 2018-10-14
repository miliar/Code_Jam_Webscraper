def main(debug):
	t=input()
	if debug==False:
		f=open('output.txt','w');
	for ti in range(t):
		line=raw_input()
		line=line.split(' ')
		kilo=float(line[0])
		h=int(line[1])
		leastTime=0
		for i in range(h):
			line=raw_input()
			line=line.split(' ')
			if (kilo-float(line[0]))/float(line[1])>leastTime:
				leastTime=(kilo-float(line[0]))/float(line[1])
		
		ret=(kilo/leastTime);
		if (debug==True):
			print("Case #{0}: {1:.7f}".format(ti+1,ret))
		else:
			f.write("Case #{0}: {1:.7f}\n".format(ti+1,ret))




if __name__=='__main__':
	main(False)