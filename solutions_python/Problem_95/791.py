#!/usr/bin/python

import sys

frq ={' ':' ','y':'a','n':'b','f':'c','i':'d','c':'e','w':'f','u':'j','b':'h','k':'i','l':'g','o':'k','m':'l','x':'m','s':'n','e':'o','v':'p','z':'q','p':'r','d':'s','r':'t','j':'u','g':'v','t':'w','h':'x','a':'y','q':'z'}
	
if 1==1:#sys.stdin.readline().rstrip("\n")=='Input':
	count = int(sys.stdin.readline(),10)
	for i in range(0,count):
		line_out=''
		line=sys.stdin.readline().rstrip("\n")
		for j in range(0,len(line)):
			line_out=line_out+frq[line[j]]
		


			
		sys.stdout.write("Case #"+str(i+1)+": "+line_out+"\n")

	

