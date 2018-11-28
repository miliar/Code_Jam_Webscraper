import networkx as nx
from random import randint
import sys

def iterator(box):
	for i in range(4):
		yield box[i]
	for i in range(4):
		yield [box[0][i],box[1][i],box[2][i],box[3][i]]
	yield [box[0][0],box[1][1],box[2][2],box[3][3]]
	yield [box[0][3],box[2][1],box[1][2],box[3][0]]
	
def line_decision(line):
	line=sorted(line)
	if line[0]==line[-1] and line[0]!='.':
		return line[0]
	if line[0]=='T' and line[-1]=='X':
		return 'X'
	if line[0]=='O' and line[-1]=='T':
		return 'O'

def make_decision(box,filled):
	for grouping in iterator(box):
		player = line_decision(grouping)
		if player:
			player
			return player+' won'
	return 'Game has not completed' if not filled else 'Draw'
		
def read_input(path):
	reader = open(path,'r')
	outfile = open('source/A-large-0.out','w')
	cases= reader.next()
	for case in range(int(cases)):
		box = []
		filled=True
		for _ in range(4):
			line = reader.next().strip()
			terms = []
			for i in line:
				if i=='.':
					filled=False
				terms.append(i)
			box+= [terms]
		print filled
		line = reader.next()
		decision = make_decision(box,filled)
		outfile.write( "Case #"+str(case+1)+": "+decision+'\n')
	outfile.close()
		

if __name__=='__main__':
	path = sys.argv[1]
	print path
	read_input(path)