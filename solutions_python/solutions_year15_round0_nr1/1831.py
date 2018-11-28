def get_min(p):
	extra=0
	total=0
	for pos,a in enumerate(p):
		extra += max(0,pos-total-extra)
		total+=a
	return extra

if __name__=="__main__":
	file="A2.in"
	with open(file) as data_file:
		data=data_file.read()
	dat=map(lambda x:x.strip(),data.split("\n"))
	cant_casos=int(dat[0])
	text=""
	for cas_num,cas in enumerate(dat[1:cant_casos+1],1):
		l=[int(f) for f in cas.split(" ")[1]]
		text+="Case #{num}: {res}\n".format(num=cas_num,res=get_min(l))
	with open("A2.out","w") as f:
		f.write(text)
