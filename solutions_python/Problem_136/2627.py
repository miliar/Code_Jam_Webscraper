#!/usr/bin/python
IN=open("B-large.in",'r')
OUT=open("output.txt",'w+')
n=int(IN.readline())

for i in range(0,n):
	row=(IN.readline().split())
	C=float(row[0])
	F=float(row[1])
	X=float(row[2])
	R_th=F*(X/C-1)
	R=2
	T=0
	while (R<R_th):
		T=T+C/R
		R=R+F
	T=T+X/R
	OUT.write("case #"+str(i+1)+": " +str(T)+"\n")

IN.close()
OUT.close()

