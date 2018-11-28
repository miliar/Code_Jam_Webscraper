def main():
	fin= open("input.in","r")
	a=fin.readline()
	fout= open("output.txt","w")
	a=a[:-1]
	a=int(a)
	
	for i in range(1,a+1):
		p1=0
		p2=0
		r1=fin.readline()
		r2=fin.readline()
		r3=fin.readline()
		r4=fin.readline()
		r1=r1[:-1]
		r2=r2[:-1]
		r3=r3[:-1]
		if fin.readline():
			r4=r4[:-1]
		r1=list(r1)
		r2=list(r2)
		r3=list(r3)
		r4=list(r4)
		r1= [ord(x) for x in r1]
		r2= [ord(x) for x in r2]
		r3= [ord(x) for x in r3]
		r4= [ord(x) for x in r4]
		
		
		for x in r1:
			if x==46:
				p1=1
				break
		for x in r2:
			if x==46:
				p1=1
				break
		for x in r3:
			if x==46:
				p1=1
				break
		for x in r4:
			if x==46:
				p1=1
				break
		
		c1=[r1[0],r2[0],r3[0],r4[0]]
		c2=[r1[1],r2[1],r3[1],r4[1]]
		c3=[r1[2],r2[2],r3[2],r4[2]]
		c4=[r1[3],r2[3],r3[3],r4[3]]
		sumr1= sum(r1)
		sumr2= sum(r2)
		sumr3= sum(r3)
		sumr4= sum(r4)
		sumc1= sum(c1)
		sumc2= sum(c2)
		sumc3= sum(c3)
		sumc4= sum(c4)
		di1=[r1[0],r2[1],r3[2],r4[3]]
		di2=[r1[3],r2[2],r3[1],r4[0]]
		sumdi1=sum(di1)
		sumdi2=sum(di2)
		lst=[sumr1,sumr2,sumr3,sumr4,sumc1,sumc2,sumc3,sumc4,sumdi1,sumdi2]
		
		for y in lst:
			if y==348 or y==352 :
				fout.write("Case #"+`i`+": X won\n")
				p2=1
				break 
			elif y==316 or y==321 :
				fout.write("Case #"+`i`+": O won\n")
				p2=1
				break
		if p2==1:
			continue
		if p2==0 and p1==1:
			fout.write("Case #"+`i`+": Game has not completed\n")
			continue
		elif p2==0 and p1==0:
			fout.write("Case #"+`i`+": Draw\n")
	fin.close()
	fout.close()					
			

if __name__=="__main__":
	main()
