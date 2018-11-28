#coding=utf-8
#!/usr/bin/env python
#--------------------------
# Google Code Jam 2012
# Qualification
# Problem A
# 2012.4.14
#--------------------------
import sys

dist={" ":" ","a":"y","b":"h","c":"e","d":"s",
"e":"o","f":"c","g":"v","h":"x","i":"d",
"j":"u","k":"i","l":"g","m":"l","n":"b",
"o":"k","p":"r","q":"z","r":"t","s":"n",
"t":"w","u":"j","v":"p","x":"m","y":"a","z":"q","w":"f"}
#== Read Part ==
def read():
	line=sys.stdin.readline()
	if line:
		return line.strip()
	else:
		sys.exit()
#== Process ==
def Pro(S):		
	sen=""
	for j in xrange(len(S)):
#		print S[j],dist[S[j]]
		sen+=dist[S[j]]
	return sen

def main():
	T=int(read())
	i=1
	while True:
		S=read()
		r=Pro(S)
		print "Case #%d: %s"%(i,r)
		if i==T:break
		i+=1

if __name__ == '__main__':
	main()
