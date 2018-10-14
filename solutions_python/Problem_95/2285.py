from string import ascii_lowercase
import sys

def process(input, rdict):
	output = ''
	for i in input:
		output += rdict[i]
	return output
		
if __name__ == '__main__':
	fname = sys.argv[1]
	rf = open(fname + '.in', 'r')
	of = open(fname + '.out', 'w')
	replaceDict = { 'y': 'a', 'e': 'o', 'q':'z','z':'q'}
	tinput = ['ejp mysljylc kd kxveddknmc re jsicpdrysi', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
			'de kr kd eoya kw aej tysr re ujdr lkgc jv']
	toutput = ['our language is impossible to understand','there are twenty six factorial possibilities',
			'so it is okay if you want to just give up']

	for i in range(3):
		inp = tinput[i]
		out = toutput[i]
		for j in range(len(inp)):
			if not replaceDict.has_key(inp[j]):
				replaceDict[inp[j]] = out[j]
	tt = int(rf.readline())
	for i in range(tt):
		input = rf.readline().strip()
		print input
		output = process(input, replaceDict)
		of.write('Case #%d: %s\n' %  (i+1, output))
		print output
	rf.close()
	of.close()
	
		
		


