#!/ms/dist/python/PROJ/core/2.5/bin/python

#http://www.astro.ufl.edu/~warner/prog/python.html
#good basic notes

import msversion
#msversion.addpkg("zope.interface","3.3.0")
#msversion.addpkg("twisted","2.5.0")
#msversion.addpkg("sybase","0.38")
#import twisted
import pickle
import math

debug = False
debugstr = ">>DEBUG>>"

count = 0 
max = 0
filestr = "/ms/user/a/alcockm/explode.in"


def reverse_Str(string):
	return string[::-1]

if(debug): print "%s found file %s" % (debugstr,filestr)
infile = open(filestr,"r")

def find_in_array(f, target):
	loc = -1
	count = 0
	for t in target:
		
		if(t==f):
		  loc = count
		  break
		count = count + 1
		
	return loc

def find_next_best(srch,count,eng,not_e):
	
	leftover = srch[count:]
	maxdist = 0
	dist = len(leftover)
	for e in eng:
		if(e == not_e):
			continue
		dist = find_in_array(e, leftover)
		if(debug): print "%s found engine: %s in: %s" % (debugstr,e,dist)
		if (dist == -1):
			best = e
			break
		if(dist > maxdist):
			maxdist = dist
			if(debug): print "%s new best is: %s" % (debugstr,e)
			best = e
	
	if(debug): print "%s next best: %s leftover: %s" % (debugstr,best,leftover)
	return best


def find_lowest_change(srch, eng):

	num = len(srch)
	
	for e in eng:
		start=e
		swcount = 0
		count = 0
		if(debug): print "%s RUNNING FOR ENGINE %s" % (debugstr,e)
		
		for s in srch:
		
			if(e==s):
				swcount = swcount + 1
				if(swcount > num):
					break
				nb = find_next_best(srch,count,eng,e)
				e = nb
				if(debug): print "%s switch count so far: %s next best: %s" % (debugstr,swcount,nb )
			
			count = count + 1
		
		if(swcount < num):
			num = swcount
			
		if(debug): print "%s done starting with: %s switches: %s" % (debugstr,e, swcount)
		
	return num


lines = infile.readlines()

loc = 0
max = int(lines[loc])
loc = loc + 1
case = 1

while (max > 0):

	engine_num = int(lines[loc])
	loc = loc + 1
	engines = []

	while (engine_num > 0):
		engines.append(lines[loc])
		loc = loc + 1
		engine_num = engine_num - 1
	
	search_num = int(lines[loc])
	loc = loc + 1
	
	searches = []
	
	while (search_num > 0):
		searches.append(lines[loc])
		loc = loc + 1
		search_num = search_num - 1
		
	if(debug): print "%s engines: %s" % (debugstr, engines)
	if(debug): print "%s searches: %s" % (debugstr, searches)
	
	num = find_lowest_change(searches, engines)
	
	output = "Case #%s: %s" % (case, num)
	print output
	
	max = max - 1
	case = case + 1

	
infile.close()

if(max==0):
	if(debug): print "%s all done" % (debugstr)
	#print "%s all done" % (debugstr)
else:
	if(debug): print "%s processed %s of %s" % (debugstr,max, max) 
	#print "%s all done" % (debugstr)
	