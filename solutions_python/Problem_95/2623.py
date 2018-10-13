#!/usr/bin/env python
import os
import sys
import string

list_output		=	[]
mapper_dict		=	{'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r' , 'q':'z',  'r':'t',  's':'n',  't':'w',
					 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a','z':'q'}
					 
def mapper(list_input_strs):
	for str in list_input_strs:
		list_output_str	=	[]
		output_string	=	""
		list_words	    =	str.split(' ')
		for word in list_words:
			new_word	=	""
			for i in range(0,len(word)):
				new_word = new_word+mapper_dict[word[i]]
			output_string	=	output_string + new_word+" "
		list_output.append(output_string)
		
		
def output_generator():
	for count in range(0,len(list_output)):
		u4_index	=	count+1
		print "Case #"+ str(u4_index)+": "+list_output[count]

		
def main():
	
	list_input_strs	= []
	f_in	=	open('A-small-attempt2.in',"r")
	doc		=	f_in.read()
	f_in.close()
	content	=	doc.split('\n')
	u4_num_inputs = content[0]
	for u4_cnt in range(1,int(u4_num_inputs)+1):
		list_input_strs.append(content[u4_cnt])
		
	
	mapper(list_input_strs)
	output_generator()
	

if __name__ == '__main__':
  main()
