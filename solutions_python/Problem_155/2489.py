#! /usr/bin/python
import sys

script_dir = "stand_ovation/"
if len(sys.argv) == 0 :
	print "ajouter argument s pour small, et l pour large"
	sys.exit()
prefix = "A"
if  len(sys.argv) > 1 and sys.argv[1] == "l":
	filename = script_dir + prefix + "-large.in"
	out = open(script_dir + prefix + '-large_out.txt', 'w')
	out.close()
	out = open(script_dir + prefix + '-large_out.txt', 'a')
	
else :
	filename = script_dir + prefix + "-small.in"
	out = open(script_dir + prefix + '-small_out.txt', 'w')
	out.close()
	out = open(script_dir + prefix + '-small_out.txt', 'a')
	
source = open(filename,'r')
nb_cases = int(source.readline())

for c in range(nb_cases) :
  #n = int(source.readline())
  linelist = source.readline().split()
  s_max = int(linelist[0])
  people = linelist[1];
  #print people
  #rslt = shynes.count('0')
  rslt  = 0
  for i in range(s_max + 1) :
	  if i != 0 : 
		standed = sum([int(elem) for elem in people[:i]])
		if i > standed :			
			people = people[:(i-1)] + str(int(people[i-1]) + 1) + people[(-(s_max + 1) + i):]			
			rslt = rslt +1
  #print s_max
  #print shynes
  #print rslt
  #print v1
  #print v2
  
  
  out.write("Case #" + str(c+1) + ": " + str(rslt))
  if c != nb_cases -1 :
	  out.write("\n")
 
out.close()
source.close()
