#!/usr/bin/env python
import sys

class NullNode: pass
class EndingNode: pass

class Node:
	def __init__(self):
		self.sons = [NullNode]*26
		
	def addSon(self,string):
		if string == "":
			return
		char = string[0]
		key = ord(char) - 97
		if len(string) > 1:
			if self.sons[key] == NullNode:
				self.sons[key]=Node()
			self.sons[key].addSon(string[1:])
		else:
			self.sons[key] = EndingNode

	def wypisz(self):
		for i in range(26):
			if self.sons[i] != NullNode:
				print chr(i+97)
				print self.sons[i].wypisz()

def parsecase(parent):
	list = [root]
	idx=0
	res=0
	for i in range(l):
		allowedLetters=[]
		if parent[idx] == '(':
			idx += 1
			while parent[idx] != ')':
				allowedLetters += [parent[idx]]
				idx+=1
			idx += 1
		else:
			allowedLetters = [parent[idx]]
			idx += 1

		tlist = list[:]
		list = []
		for i in tlist:
			for j in allowedLetters:
				node = i.sons[ord(j)-97]
				if node != NullNode:
					if node == EndingNode:
						res += 1
					else:
						list += [node]
	return res

l = 0
d = 0
n = 0

(l, d, n) = [int(n) for n in sys.stdin.readline().split(" ")]

root=Node()

for i in range(d):
	root.addSon(sys.stdin.readline()[:l])

for i in range(n):
	print "Case #{0}: {1}".format(i+1,parsecase(sys.stdin.readline()))
