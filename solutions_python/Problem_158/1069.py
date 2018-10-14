def prod(x,r,c):
	if x==1:
		return "GABRIEL"
	if x==2:
		if r*c%2==0: 
			return "GABRIEL"
		else:
			return "RICHARD"
	if x==3:
		if r*c in [6,9,12]:
			return "GABRIEL"
		else:
			return "RICHARD"
	if x==4:
		if r*c in [12,16]:
			return "GABRIEL"
		else:
			return "RICHARD"


if __name__=="__main__":
	file="D2.in"
	with open(file) as data_file:
		data=data_file.read()
	dat=map(lambda x:x.strip(),data.split("\n"))
	cant_casos=int(dat[0])
	text=""
	for cas_num,cas in enumerate(dat[1:cant_casos+1],1):
		x=int(cas.split(" ")[0])
		r=int(cas.split(" ")[1])
		c=int(cas.split(" ")[2])
		text+="Case #{num}: {res}\n".format(num=cas_num,res=prod(x,r,c))
	with open("D2.out","w") as f:
		f.write(text)
