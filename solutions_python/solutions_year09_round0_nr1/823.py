'''
Created on Sep 2, 2009

@author: Adam
'''

from copy import deepcopy
import time

groups = []
reqstr = []
pos_list = []
words = set()
poss = set()

def processWords(file):
	global groups
	global reqstr
	global pos_list
	
	wordlen, numex, cases = map(int, file.readline().split())
	
	for i in range(numex):
		words.add(file.readline().strip())
		
	buildPosList(wordlen)
	
	for i in range(cases):
		groups = []
		reqstr = []
		poss = getAllPossibles(file.readline().strip())
		print("Case #" + str(i+1) + ": " + str(poss))
		#time.sleep(2)
		
def buildPosList(wordlen):
	global pos_list
	
	pos_list = [set() for i in range(wordlen)]
	
	for word in words:
		for i in range(wordlen):
			pos_list[i].add(word[i])
		
	x = 1	
	for list in pos_list:
		x = x * len(list)
		
	#print('pos_list:<' + str(pos_list) + '>')
	#print('num perms:' + str(x))

def getAllPossibles(word):
	global poss
	
	splitWord(word)
	poss = words.copy()
	
	for string in reqstr:
		for word in words:
			if word.find(string) == -1:
				poss.remove(word)
			
	return len(poss.intersection(buildPermutations()))
	
def splitWord(word):
	global groups
	global reqstr
	curword = ''
	curgroup = []
	group = False
	
	for ch in word:
		if ch == '(':
			group = True
			groups.extend(curword)
			reqstr.append(curword)
			curword = ''
		elif ch == ')':
			group = False
			groups.append(curgroup)
			curgroup = []
		elif group:
			curgroup.append(ch)
		else:
			curword = curword + ch
	
	if len(curword) > 0:
		groups.extend(curword)
		
	groups = [elem for elem in groups if elem != '']
	reqstr = [elem for elem in reqstr if elem != '']
	
def buildPermutations():
	perms = ['']
	
	#print('Groups:<' + str(groups) + '>')
	
	for wordindex in range(len(groups)):
		#print('Index:' + str(wordindex))
		#print("perms:<" + str(perms) + '>')
		block = groups[wordindex]
		
		if len(block) > 1:
			newperms = []
			for i in range(len(block)):
				newperms.extend(perms)
				
			#print('Newperms:<' + str(newperms) + '>')
				
			for x in range(len(block)):
				ch = block[x]
				
				#print('Testing char <' + ch + '> at pos <' + str(x) + '>')
				
				if ch in pos_list[wordindex]:
					for y in range(len(perms)):
						index = y + (x * len(perms))
						newword = newperms[index] + ch
						newperms[index] = newword
				
				#print('Newperms:<' + str(newperms) + '>')
						
			perms = [elem for elem in set(newperms) if len(elem) > wordindex]
			cuts = []
			
			for perm in perms:
				ok = False
				for elem in poss:
					if elem.startswith(perm):
						ok = True
						break
				if not ok:
					cuts.append(perm)
			
			for cut in cuts:
				perms.remove(cut)
				
			if len(perms) == 0:
				break
				
		elif block in pos_list[wordindex]:
			for i in range(len(perms)):
				perms[i] = perms[i] + block
		else:
			break
	
	return set(perms)

if __name__ == '__main__':
	with open("A-small-attempt1.in") as f:
		processWords(f)