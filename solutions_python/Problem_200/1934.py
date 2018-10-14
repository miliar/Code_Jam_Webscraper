# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:13:27 2017

@author: Billoier
"""
def check(l,st):
	for i in range(st,len(l)-1):
		if(l[i]<l[i+1]):
			return False
	return True

def Transform(l,st):
#	ago = -1;
	for i in range(st,len(l)):
		l[i] = str(int(l[i])-1);
		if(l[i]>='0'):
			break;
		else:
			l[i] = '9';
	i = len(l)-1;
	while(i>=0):
		if(l[i]!='0'):
			break;
		del l[i];
		i-=1;
	return l;

if __name__=='__main__':
	Test_Num = int(input().strip());
	for i in range(Test_Num):
		MaxValue = list(input().strip());
		MaxValue.reverse();
		for j in range(len(MaxValue)):
			if(check(MaxValue,j)):
				print('Case #'+str(i+1)+': '+''.join(MaxValue[::-1]));
				break;
			else:
				MaxValue[j] = '9';
				MaxValue  = Transform(MaxValue,j+1);




