#!/usr/bin/python
"""
lawnmower.py

google code jam

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
	# Open files
	w = open("output.txt", 'w')
	f = open("workfile.txt", 'r')
	T = int(f.readline())
	
	for i in range(T):
		buff = f.readline().split()
		N = int(buff[0])
		M = int(buff[1])
		
		# Load into arr
		arr = []
		for n in range(N):
			arr.append(f.readline().rstrip().split())
		for a in arr:
			print a
		
		# check for maximum in row and column
		possible = True
		for n in range(N):
			for m in range(M):
				rowPos = True
				colPos = True
				
				# check for max in row
				if max(arr[n]) > arr[n][m]:
					rowPos = False
				
				# check for max in column
				for x in range(N):
					if arr[x][m] > arr[n][m]:
						colPos = False
						break
				
				if rowPos == False and colPos == False:
					possible = False
					break
			
			if possible == False:
				break
			
		if possible == False:
			w.write("Case #"+str(i+1)+": NO\n")
			print "Case #"+str(i+1)+": NO"
		else:
			w.write("Case #"+str(i+1)+": YES\n")
			print "Case #"+str(i+1)+": YES"
			 
		
if __name__ == '__main__':
	main()
	