#!/usr/bin/python
#Author : Atharva Chauthaiwale 

import sys
import re

	
def main_logic(word):
	print word	
	l=[]
	for i in range(0,len(word)):
		if word[i] in l:
			continue	
		else:
		   l.append(word[i])		
	print l
	f=0
	if len(l)>1:
		t=l[0]
		l[0]=l[1]
		l[1]=t
		base=len(l);
		print base
	else:
	      base=2
	      f=1		
	      print base		
        
	res=0
	for j in range(0,len(word)):
		if f==1:
			ind=1
		else:
			ind=l.index(word[j])
		
		#print 'index of %s is %d' %(word[j],ind)
		exp=len(word)-1-j
		#print exp
		res+=ind*base**(exp)

	print res

	return res
		
def get_input(args):
        f=file(args[0])
        first_line=f.readline()
	N=int(first_line[0])
	
	f1=file('result.txt','w')	
        print "N= %d" %N 
        for i in range(0,100):
		word=f.readline()
		#print word
		word=word.replace('\n','')
	       	res=main_logic(word) # 

		nres="Case #%d: %d\n" %(i+1,res)
		f1.write(nres)
		#print res		
	f1.close()
		
print 'code jam program'
args=sys.argv[1:]
get_input(args)


