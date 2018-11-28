#!/usr/bin/env python2.6
'''
Created on 03/set/2009

@author: marco
'''
import sys
import re

def explore(currentX,currentY,sizeX,sizeY):
	retval=[]
	if(currentY>0):
		retval.append((currentX,currentY-1))
	if(currentX>0):
		retval.append((currentX-1,currentY))
	if(currentX+1<sizeX):
		retval.append((currentX+1,currentY))
	if(currentY+1<sizeY):
		retval.append((currentX,currentY+1))

	assert(len(retval)<=4)
	return retval

#def isMinor(map,posX,posY,cValue):

if __name__ == '__main__':
	
	inp = open(sys.argv[1], 'r')
	out = open(sys.argv[2], 'w')
	
	line = inp.readline()
	T=int(line)
	
	for map_it in range(T):
		basinDB={}
		lettersDB={}
		map=[]
		line = inp.readline().rstrip("\n").split()
		sizeX=int(line[1])
		sizeY=int(line[0])
		
		for cmap in range(sizeY):
			line = inp.readline().rstrip("\n").split()
			for n in range(len(line)):
				line[n]=float(line[n])
			
			map.append(line)
		
		for currentY in range(sizeY):
			for currentX in range(sizeX):
				toExp=explore(currentX,currentY,sizeX,sizeY)
				min_x=currentX
				min_y=currentY
				min_val=map[currentY][currentX]
				for cell in toExp:
					if(map[cell[1]][cell[0]] < min_val):
						min_val=map[cell[1]][cell[0]]
						min_x=cell[0]
						min_y=cell[1]

				
				if(basinDB.has_key((min_x,min_y)) and not basinDB.has_key((currentX,currentY))):
					basinDB[(min_x,min_y)].add((currentX,currentY))
					basinDB[(currentX,currentY)]=basinDB[(min_x,min_y)]
				elif(basinDB.has_key((min_x,min_y)) and basinDB.has_key((currentX,currentY))):
					basinDB[(min_x,min_y)].update(basinDB[(currentX,currentY)])
					for toUp in basinDB[(currentX,currentY)]:
						basinDB[toUp]=basinDB[(min_x,min_y)]
				elif(basinDB.has_key((currentX,currentY)) and not basinDB.has_key((min_x,min_y))):
					basinDB[(currentX,currentY)].add((min_x,min_y))
					basinDB[(min_x,min_y)]=basinDB[(currentX,currentY)]
				else:
					basinDB[(currentX,currentY)]=set()
					basinDB[(currentX,currentY)].add((min_x,min_y))
					basinDB[(currentX,currentY)].add((currentX,currentY))
					basinDB[(min_x,min_y)]=basinDB[(currentX,currentY)]
		
		curr_letter=97
		out.write("Case #%d:\n"%(map_it+1))
		for currentY in range(sizeY):
			for currentX in range(sizeX):
				currentID=(currentX,currentY)
				if(not lettersDB.has_key(currentID)):
					for i in basinDB[currentID]:
						lettersDB[i]=chr(curr_letter)
					curr_letter+=1
				out.write("%c"%lettersDB[currentID])
				if(currentX+1<sizeX):
					out.write(" ")
				else:
					out.write("\n")
