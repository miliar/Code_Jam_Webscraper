#!/usr/bin/python
# -*- coding: utf-8 -*-

def compute_nb_friends_needed(line):
	Smax = int(line[0]) # max shy level

	nb_friends_needed = 0
	if (Smax != 0):
		shyness_levels_count = [int(d) for d in line[1]]
		total = sum(shyness_levels_count)
		standing_up = shyness_levels_count[0]
		for lvl in range(1,Smax+1):
			if standing_up < lvl:
				nb_friends_needed += lvl-standing_up
				standing_up = lvl
			standing_up += shyness_levels_count[lvl]
			# print line[1]+' (%d: %d,%d)'%(lvl,standing_up,nb_friends_needed)
	return nb_friends_needed

def main():
	# filestr = 'A-small-attempt1'
	filestr = 'A-large'
	# filestr = 'A-verysmall'
	fin = open(filestr+'.in.txt','r')
	fout = open(filestr+'.out','w')

	lines = fin.read().splitlines()
	T = int(lines[0])
	for i in range(T):
		line = lines[i+1].split(' ')
		nb_friends_needed = compute_nb_friends_needed(line)
		str=  'Case #%d: %d'%(i+1,nb_friends_needed)
		fout.write(str+'\n')
		print str

	fin.close()
	fout.close()


if __name__ == "__main__":
	main()
