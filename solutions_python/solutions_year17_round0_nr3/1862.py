# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 00:32:09 2017

@author: Billoier
"""
T = list();
from math import *
def Get_Ans(key):
	if(key & 1):
		return key>>1,key>>1;
	else:
		return (key>>1)-1,key>>1;


if __name__=='__main__':
	Test_Num = int(input().strip());
	for i in range(Test_Num):
		line = input().strip();
		n = int(line.split(' ')[0].strip());
		k = int(line.split(' ')[1].strip());
		
		
		T = [0]*(1<<(int(log2(k))+1));
		T[0] = k;
		T[1] = n;
		st = 1<<(int(log2(k)));

		for j in range(1,st):
			if(T[j] & 1):
				T[j<<1] = T[j]>>1;
				T[(j<<1) + 1] = T[j<<1];
			else:
				T[j<<1] = (T[j]>>1) -1;
				T[(j<<1) +1 ] = T[j]>>1;
         
		son = T[st:(st<<1)];
		son = sorted(son,reverse = True);
		key = son[k-st];
		ls,rs = Get_Ans(key);

		print('Case #'+str(i+1)+': '+str(max(ls,rs))+' '+str(min(ls,rs)));
		T.clear();
