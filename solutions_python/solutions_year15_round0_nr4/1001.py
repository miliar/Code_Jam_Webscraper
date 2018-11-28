#!/usr/bin/python3
import ipdb
data=open("input")
output_file=open("output", "w")
n=data.readline()[0:-1]
testdata=data.readlines()
tt=0
for t in testdata:
		win=''
		test=t[0:-1]
		(x1,r1,c1)=test.split()
		x=int(x1)
		r=int(r1)
		c=int(c1)
		if (x>6):
				win=": RICHARD"
		elif (x>r*c):
				win=": RICHARD"
		elif (x>r*c):
				win=": RICHARD"
		elif (x==r*c):
				if (x==1)|(x==2):
						win=": GABRIEL"
				else :
						win=": RICHARD"
		elif ((x<r*c) & (x>(r*c/2))):
				win=": RICHARD"
		elif (x==(r*c)/2):
				if (x==1):
						win=": GABRIEL"
				elif (x==2):
						win=": GABRIEL"
				elif (x==3):
						if ((r>=2) & (c%3 ==0))|((c>=2) & (r%3==0)):
								win=": GABRIEL"
						else:
								win=": RICHARD"
				elif (x==4):
						if ((r>=3) & (c%4 ==0)) | ((c>=3) & (r%4==0)):
								win=": GABRIEL"
						else:
								win=": RICHARD"
				elif (x==5):
						if ((r>=4) & (c%5 ==0))|((c>=4) & (r%5==0)):
								win=": GABRIEL"
						else:
								win=": RICHARD"
				elif (x==6):
						if ((r>=5) & (c%6 ==0))|((c>=5) & (r%6==0)):
								win=": GABRIEL"
						else:
								win=": RICHARD"
		elif (x<(r*c)/2 ):
				if((r*c)%x==0):
						if x==1:
								win=": GABRIEL"
						if x==2:
								win=": GABRIEL"
						elif (x==3 ):
								if((r>=2) & (c%3==0)) |((c>=2) & (r%3==0)):
										win=": GABRIEL"
								else:
										win=": RICHARD"
						elif (x==4 ):
								if((r>=3) & (c%4==0)) |((c>=3) & (r%4==0)):
										win=": GABRIEL"
								else:
										win=": RICHARD"
						elif (x==5 ):
								if((r>=4) & (c%5==0)) |((c>=4) & (r%5==0)):
										win=": GABRIEL"
								else:
										win=": RICHARD"
						elif (x==6 ):
								if((r>=5) & (c%6==0)) |((c>=5) & (r%6==0)):
										win=": GABRIEL"
								else:
										win=": RICHARD"
				else:
						win=": RICHARD"
		tt+=1
		if (win==""):
				ipdb.set_trace()
		print("Case #"+str(tt)+win,file=output_file)

