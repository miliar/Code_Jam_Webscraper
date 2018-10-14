import re
import sys


def baseconvert(n, base):
#convert positive decimal integer n to equivalent in another base (2-36)"""

        digits = "0123456789abcdefghijklmnopqrstuvwxyz"

        try:
                n = int(n)
                base = int(base)
        except:
                return ""

        if n < 0 or base < 2 or base > 36:
                return ""

        s = ""
        while 1:
                r = n % base
                s = digits[r] + s
                n = n / base
                if n == 0:
                        break
        return s

f=open(sys.argv[1])
a=f.readline()
a=re.sub('\n','',a)
b=re.split('\ ',a)
D=int(b[0])
c=''
finalAnswer=''
for i in range(D):
        c=f.readline();
	d=re.sub('\n','',c)
	e=re.split('\ ',d)
	g=str(baseconvert(e[1],2))
	h=int(e[0])
	ON=str(1)*int(e[0])
	if g == str(0):
		answer=0
	elif len(g) < int(e[0]):
		answer=0
	else:
		for j in range(int(e[0])):
			try:
				if j == 0:
					answer=(str(g[len(g)-j-1]))
				else:
					answer=str(g[len(g)-j-1])+str(answer)
			except:
				answer=0
#	if answer==0:
#		finalAnswer='OFF'
	if answer==ON:
		finalAnswer='ON'
	else:
		finalAnswer='OFF'
	print 'Case #' + str(i+1) + ': ' + finalAnswer
