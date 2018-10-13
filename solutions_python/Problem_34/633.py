#!/usr/bin/python
#Author : Atharva Chauthaiwale 

import sys
import re

def find_patt(D,N,wlist,plist):
	f=file('result.txt','w')	
	for i in range(0,N):
		pat=plist[i]
		pat=pat.replace('(','[')
		pat=pat.replace(')',']')
		found=0
		for j in range(0,D):
			if re.search(pat,wlist[j]) :
				found+=1
		res='Case #%d:  %d\n' %(i+1,found) 			
		print res
		f.write(res)
	f.close()
		
def get_input(args):
        f=file(args[0])
        first_line=f.readline()
	ldn_list=first_line.split()
	L=int(ldn_list[0])
	D=int(ldn_list[1])
	N=int(ldn_list[2])
	word_list=[]
	print "%d %d %d" %(L,D,N)
        for i in range(0,D):
		word=f.readline()
		word=word.replace('\n','')
		word_list.append(word)	
 
	print word_list
          
        pat_list=[]

	for j in range(0,N):
		pat=f.readline()
		pat=pat.replace('\n','')
		pat_list.append(pat)
	print pat_list	
	
	find_patt(D,N,word_list,pat_list)

	
print 'alien code jam program'
args=sys.argv[1:]
get_input(args)


