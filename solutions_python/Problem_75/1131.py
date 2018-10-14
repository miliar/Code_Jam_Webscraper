#!/usr/bin/python

import sys
import string
import math

#robot class for keeping track of place and timesense last move
class Commands:
	def __init__(self,Combine,Oppose):

		### Combine
		self.combine={}
		for i in range(len(Combine)):
			self.combine[Combine[i][0:2]]=Combine[i][2]
		self.combine_keys = list(self.combine.viewkeys())
		### Oppose
		self.oppose={}
		for i in range(len(Oppose)):
			self.oppose[Oppose[i][0]]=Oppose[i][1]
			self.oppose[Oppose[i][1]]=Oppose[i][0]
		self.oppose_keys = list(self.oppose.viewkeys())

		#Element List
		self.ElementsList=[]

	def clear(self,invoked):
		for i in range(len(self.ElementsList)):
			if self.oppose_keys.count(invoked)==1:
				if self.oppose[invoked]==self.ElementsList[i]:
						self.ElementsList=[]
						return True
		return False

	#look for combinations then update Element list if the is a combination
	def transform(self,invoked,Elements):
		if len(self.ElementsList)>0:
			for i in self.combine_keys:
				if (i == self.ElementsList[-1]+invoked) or (i == invoked + self.ElementsList[-1]):
					self.ElementsList[-1]=self.combine[i]
			
					return True
		return False
				

	def extend_list(self,A):
		self.ElementsList.append(A)


#do a single run
def do_one_case(cnum):
	#Parse single line
	M = sys.stdin.readline().split()
	nCombine = int(M[0])
	Combine  = M[1:1+nCombine]
	nOppose = int(M[nCombine+1])
	Oppose = M[nCombine+2:-2]
	nElements = M[-2]
	Elements = list(M[-1]+'1')

	#wizzard is the one who invokes things
	wizzard = Commands(Combine,Oppose)
	#wizzard.extend_list(Elements.pop(0))
	invoked = Elements[0]


	#Main Logic
	while invoked!='1':
		if wizzard.transform(invoked,Elements):
			Elements.pop(0)
		else:
			if wizzard.clear(invoked):
				Elements.pop(0)
			else:
				wizzard.extend_list(Elements.pop(0))
		invoked = Elements[0]

	string = 'Case #%i: '%cnum + str(wizzard.ElementsList)+'\n'
	string = string.replace("'","")
	print string




def main():
	N = int(sys.stdin.readline().strip())
	for i in range(N):
		do_one_case(i+1)


if __name__ == "__main__":
	main()
