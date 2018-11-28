
def main(line):
	s=''
        z=len(line)+1
	for x in xrange(z):
	  n=line[x-1]
	  if n == 'a':
	      s = s[:x-1] + 'y' + s[x:]
	  elif n == 'b' :
	      s = s[:x-1] + 'h' + s[x:]
	  elif n == 'c' :
	      s = s[:x-1] + 'e' + s[x:]
	  elif n == 'd' :
	      s = s[:x-1] + 's' + s[x:]
	  elif n == 'e' :
	      s = s[:x-1] + 'o' + s[x:]
	  elif n == 'f' :
	      s = s[:x-1] + 'c' + s[x:]
	  elif n == 'g' :
	      s = s[:x-1] + 'v' + s[x:]
	  elif n == 'h' :
	      s = s[:x-1] + 'x' + s[x:]
	  elif n == 'i' :
	      s = s[:x-1] + 'd' + s[x:]
	  elif n == 'j' :
	      s = s[:x-1] + 'u' + s[x:]
	  elif n == 'k' :
	      s = s[:x-1] + 'i' + s[x:]
	  elif n == 'l' :
	      s = s[:x-1] + 'g' + s[x:]
	  elif n == 'm' :
	      s = s[:x-1] + 'l' + s[x:]
	  elif n == 'n' :
	      s = s[:x-1] + 'b' + s[x:]
	  elif n == 'o' :
	      s = s[:x-1] + 'k' + s[x:]
	  elif n == 'p' :
	      s = s[:x-1] + 'r' + s[x:]
	  elif n == 'q' :
	      s = s[:x-1] + 'z' + s[x:]
	  elif n == 'r' :
	      s = s[:x-1] + 't' + s[x:]
	  elif n == 's' :
	      s = s[:x-1] + 'n' + s[x:]
	  elif n == 't' :
	      s = s[:x-1] + 'w' + s[x:]
	  elif n == 'u' :
	      s = s[:x-1] + 'j' + s[x:]
	  elif n == 'v' :
	      s = s[:x-1] + 'p' + s[x:]
	  elif n == 'w' :
	      s = s[:x-1] + 'f' + s[x:]
	  elif n == 'x' :
	      s = s[:x-1] + 'm' + s[x:]
	  elif n == 'y' :
	      s = s[:x-1] + 'a' + s[x:]
	  elif n == 'z' :
	      s = s[:x-1] + 'q' + s[x:]
	  else:
	      s = s[:x-1] + n + s[x:]
        return s


if __name__ == '__main__':
	import sys
	N = int(sys.stdin.readline())
	for i in xrange(N):
		res = main(sys.stdin.readline().strip())
		print "Case #%d: %s" % (i + 1, res)	
