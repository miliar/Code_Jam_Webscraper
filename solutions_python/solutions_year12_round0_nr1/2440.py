import sys

alfabet=['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']

def main():
	c=0
	tc=int(raw_input())
	while c<tc:
		txt=raw_input()
		out=''
		for i in txt:
			if ord(i)>=ord('a') and ord(i)<=ord('z'):
				out=out+alfabet[ord(i)-ord('a')]
			else:
				out=out+i
		sys.stdout.write("Case #%d: %s\n" % (c+1,out))
		c=c+1
	
main()
