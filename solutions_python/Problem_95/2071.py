import sys

def convert(str):
        l = len(str)
        for i in range(l):
                if str[i]==' ':
                        sys.stdout.write(str[i])
                else:
                        sys.stdout.write(dic[str[i]])




dic = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q'}

t = int(raw_input())

for i in range(t):
	str = raw_input()
	print "Case #%d: " % (i+1),
	convert(str)
	print ''
