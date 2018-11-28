#!/usr/bin/python
"""
tictactoe

google code jam #1

Date: April 13, 2013
"""
# Imports
import sys, os

__version__ = "0.0"
__copyright__ = "CopyRight (C) 2012-13 by Coding Assassin"
__license__ = "MIT"
__author__ = "Coding Assassin"
__author_email__ = "Coding Assassin, codingassassin@gmail.com"

USAGE = "%prog [options]"
VERSION = "%prog v" + __version__

AGENT = "%s/%s" % (__name__, __version__)

def main():
	# open file
	w = open("output.txt", 'w')
	f = open('workfile.txt', 'r')
	num = int(f.readline())
	
	for i in range(num):
		# Load Array
		arr = []
		for x in range(4):
			arr.append(list(f.readline().rstrip()))
		f.readline()
		
		# Check for horizontal
		horiz = True
		for j in range(4):
			horiz = True
			for k in range(3):
				if arr[j][k] != arr[j][k+1] and arr[j][k] != 'T' and arr[j][k+1] != 'T':
					horiz = False
				
				if arr[j][k] == '.' or arr[j][k+1] == '.':
					horiz = False
			if horiz:
				if arr[j][0] == 'T':
					arr[j][0] = arr[j][1]
				w.write("Case #"+str(i+1)+": "+arr[j][0]+" won\n")
				print "Case #"+str(i+1)+": "+arr[j][0]+" won"
				break
		
		if horiz:
			continue
		
		# check verticals
		vert = True
		for j in range(4):
			vert = True
			for k in range(3):
				if arr[k][j] != arr[k+1][j] and arr[k][j] != 'T' and arr[k+1][j] != 'T':
					vert = False
				if arr[k][j] == '.' or arr[k+1][j] == '.':
					vert = False
			if vert:
				if arr[0][j] == 'T':
					arr[0][j] = arr[1][j]
				print "Case #"+str(i+1)+": "+arr[0][j]+" won"
				w.write("Case #"+str(i+1)+": "+arr[0][j]+" won\n")
				break

		if vert:
			continue
		
		# check for top left to bottom right
		diag = True
		for j in range(3):
			if arr[j][j] != arr[j+1][j+1] and arr[j][j] != 'T' and arr[j+1][j+1] != 'T':
				diag = False
			if arr[j][j] == '.' or arr[j+1][j+1] == '.':
				diag = False
		
		if diag:
			if arr[0][0] == 'T':
				arr[0][0] = arr[1][1]
			print "Case #"+str(i+1)+": "+arr[0][0]+" won"
			w.write("Case #"+str(i+1)+": "+arr[0][0]+" won\n")
		
		if diag:
			continue
		
		# check for top right to bottom left
		diag = True			
		for j in range(3):
			if arr[j][3-j] != arr[j+1][2-j] and arr[j][2-j] != 'T' and arr[j+1][2-j] != 'T':
				diag = False
			if arr[j][3-j] == '.' or arr[j+1][2-j] == '.':
				diag = False
		
		if diag:
			if arr[0][3] == 'T':
				arr[0][3] = arr[1][2]
			print "Case #"+str(i+1)+": "+arr[0][3]+" won"
			w.write("Case #"+str(i+1)+": "+arr[0][3]+" won\n")
		
		if diag:
			continue
		
		draw = True
		for j in range(4):
			for k in range(4):
				if arr[j][k] == '.':
					draw = False
		
		if draw:
			print "Case #"+str(i+1)+": Draw"
			w.write("Case #"+str(i+1)+": Draw\n")
		else:
			print "Case #"+str(i+1)+": Game has not completed"
			w.write("Case #"+str(i+1)+": Game has not completed\n")
		
	f.close()
	w.close()
		
if __name__ == '__main__':
	main()