def findMinimum(row):
	total=0
	count=0
	for i in range(len(row)):
		if(i-total>0):
			count+=1
			total+=1
		total=total+int(row[i])
	return count

def main():
	txt = open('/home/nithin/GoogleCodeJam/A-large.txt')
	lines = txt.read().split('\n')
	for j in range(1,int(lines[0])+1):
		inp=lines[j].split(" ")
		val=inp[1]
		out=findMinimum(val)
		print "Case #"+str(j)+": "+str(out) 
if __name__ == '__main__':
	main()

