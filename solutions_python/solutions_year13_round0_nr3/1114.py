import sys, math

def main():
	cases = int( sys.stdin.readline().strip() )

	for c in range(0,cases):
		[l,h] = sys.stdin.readline().strip().split()

		tmp = 0
		for i in range(int(l),int(h)+1):
			if str(i) == str(i)[::-1]:
				a = math.sqrt(i)
				b = math.floor(a)
				if ( a == b ) and ( str(b) == str(b)[::-1] ):
					tmp += 1

		print( "Case #%s: %s" % (c+1,tmp) )

if __name__ == '__main__':
	main()