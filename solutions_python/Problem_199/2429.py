def main(deb):

	n = input()
	f = open('output.txt','w')
	for i in range(n):
		imp=False
		count=0
		text=raw_input()
		pans=text.split(" ")[0]
		pans=list(pans)
		size=int(text.split(" ")[1])
		for j in range(len(pans)-size+1):
			if(pans[j]=='-'):
				count+=1
				for k in range(size):
					pans[j+k]=rev(pans[j+k])
		for j in range(size-1):
			if(pans[len(pans)-j-1]=='-'):
				if deb==True:
					print("Case #{}: IMPOSSIBLE".format(i+1))
				else:
					f.write("Case #{}: IMPOSSIBLE\n".format(i+1))
				imp=True
				break
		if imp==True:
			continue
		if deb==True:
			print("Case #{}: {}".format(i+1,count))
		else:
			f.write("Case #{}: {}\n".format(i+1,count))

	f.close();

def rev(inp):
	if inp=='+':
		return '-'
	else:
		return '+'

if __name__ == "__main__":
	main(False)
