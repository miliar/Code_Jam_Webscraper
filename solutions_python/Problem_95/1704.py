import sys
import pprint
import json
import re

if(len(sys.argv) > 1):

	f = open(sys.argv[1])
	cases = f.readline().strip()
	d_f = open('dict.in').read()
	d_s = re.sub("[']",'"',d_f)
	d = json.loads(d_s)

	for i in range((int)(cases)):
		line = f.readline().strip()
		new_line = ""
		
		for j in range(len(line)):
			if(line[j] == ' '):
				new_line+= ' '
			else:
				new_line+=d[line[j]]

		print "Case #"+((str)(i+1))+": "+new_line
