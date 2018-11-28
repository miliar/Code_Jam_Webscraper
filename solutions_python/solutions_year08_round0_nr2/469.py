from operator import itemgetter

iFile=open("/home/knuthy/Desktop/B-large.in","r")
txt=iFile.read()
iFile.close()
input=txt.split('\n')
cases=int(input[0])
if input[-1]=='':
	input=input[:-1]

pos=1

outputFile=open("outputLarge","w")
def toMin(h):
	return int(h[:2])*60+int(h[3:])

	
for case in range(1,cases+1):
	T=int(input[pos])
	NA,NB=input[pos+1].split()
	NA=int(NA)
	NB=int(NB)
	finA=0
	finB=0
	#get dep and arv for each NA
	startNA=pos+2
	endNA=startNA+NA
	A=[]
	for line in input[startNA:endNA]:
		line=line.split()
		A.append({"dep":toMin(line[0]),"arv":toMin(line[1]),"src":"A","done":False})
	
	#get dep and arv for each NB
	startNB=endNA
	endNB=startNB+NB
	B=[]
	for line in input[startNB:endNB]:
		line=line.split()
		B.append({"dep":toMin(line[0]),"arv":toMin(line[1]),"src":"B","done":False})
	All=A
	All.extend(B)
	All = sorted(All, key=itemgetter('dep'))
	
	#arrival=0
	
	for timeline in All:
		TL=timeline
		if TL["done"]!=True:
			#print "=%s"%TL
			TL["done"]=True
			arv=TL["arv"]+T
			src=timeline["src"]
			if src=="A":
				finA=finA+1
			else:
				finB=finB+1
			
			for tl in All:
				#print "_%s_%s"%(tl,arv)
				if tl["dep"]>=arv and tl["src"]!=src and tl["done"]!=True:
					TL=tl
					arv=TL["arv"]+T
					src=TL["src"]
					tl["done"]=True
				
		

	print "Case #%s: %s %s"%(case,finA,finB)
	outputFile.write("Case #%s: %s %s\n"%(case,finA,finB))
	pos=endNB
outputFile.close()

