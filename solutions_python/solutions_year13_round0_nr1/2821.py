import re, sys

def eOiI ():
	print("No valid input given!")
	sys.exit(1)

def strip (s):
	return s.strip()

f = open("input.in")
s = f.readline()
m = re.search('^\s*(\d+)\s*$', s)

if m == None:
	eOiI()
c = int(m.group(1))+1
for i in range(1,c):
	s = ''.join([f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip()])
	m = re.search('^(.{4}|.{8}|.{12})?[XT]{4}|(([XT]).{3}){4}|.(([XT]).{2}){4}|(.{2}([XT]).){4}|(.{3}([XT])){4}|([XT].{4}){3}[XT]|.(.{2}[XT]){4}.{3}$', s)
	if m:
		print('Case #{0}: X won'.format(i))
	else:
		m = re.search('^(.{4}|.{8}|.{12})?[OT]{4}|(([OT]).{3}){4}|(.([OT]).{2}){4}|(.{2}([OT]).){4}|(.{3}([OT])){4}|([OT].{4}){3}[OT]|.(.{2}[OT]){4}.{3}$', s)
		if m:
			print('Case #{0}: O won'.format(i))
		elif '.' in s:
			print('Case #{0}: Game has not completed'.format(i))
		else:
			print('Case #{0}: Draw'.format(i))
	s = f.readline()
	  
