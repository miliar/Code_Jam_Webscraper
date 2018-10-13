import sys

d = { 'y':'a', 'n':'b', 'f':'c', 'i':'d', 'c':'e', 'w':'f', 'l':'g', 'b':'h', 'k':'i', 'u':'j', 'o':'k', 'm':'l', 'x':'m',
	  's':'n', 'e':'o', 'v':'p', 'z':'q', 'p':'r', 'd':'s', 'r':'t', 'j':'u', 'g':'v', 't':'w', 'h':'x', 'a':'y', 'q':'z'}

def googlerese(s,d):
	ns = ''
	for i in s:
		if i in d:
			ns += d[i]
		else:
			ns += i
	return ns

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
    lines =[line.strip() for line in open(fn)]
    lines.pop(0)
    
    for line in range(len(lines)):
		print "Case #"+str(line+1)+": "+googlerese(lines[line],d)
