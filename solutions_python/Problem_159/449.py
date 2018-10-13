def main(line):
	pan=map(lambda x:int(x),line.split(" "))
	return str(maxim(pan)) + " " + str(prom(pan))

def prom(pan):
	max=0
	for i,x in enumerate(pan,1):
		if len(pan)==i: continue
		if x-pan[i]>max:
			max=x-pan[i]
	lost=0
	for i,x in enumerate(pan,1):
		if len(pan)==i: continue
		if x<max:
			lost+=max-x
	return (len(pan)-1)*max-lost

def maxim(pan):
	tot=0
	for i,x in enumerate(pan,1):
		if len(pan)==i: continue
		if x>pan[i]:
			tot+=x-pan[i]
	return tot

if __name__=="__main__":
	file="/home/gaston/Downloads/A.in"
	with open(file) as data_file:
		data=data_file.read()
	dat=map(lambda x:x.strip(),data.split("\n"))
	cant_casos=int(dat[0])
	text=""
	for cas_num,line in enumerate(dat[1:],1):
		if cas_num%2==1:
			continue
		text+="Case #{num}: {res}\n".format(num=cas_num/2,res=main(line))
	print text
	with open("/home/gaston/A.out","w") as f:
		f.write(text)
