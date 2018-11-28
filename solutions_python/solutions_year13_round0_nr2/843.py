import sys

def main():
	cases = int( sys.stdin.readline().strip() )

	for c in range(0,cases):
		[i,j] = sys.stdin.readline().strip().split(" ")

		tmp = []
		for line in range(0,int(i)):
			tmp.append( sys.stdin.readline().strip().split(" ") )

		print( "Case #%s: %s" % (c+1,check(int(i),int(j),tmp)) )

def check(i,j,tmp):
	for a in range(0,i):
		for b in range(0,j):
			badRow = False
			badCol = False

			for y in range(0,j):
				if int(tmp[a][y]) > int(tmp[a][b]):
					badRow = True
					break	

			for x in range(0,i):
				if int(tmp[x][b]) > int(tmp[a][b]):
					badCol = True
					break

			if badRow and badCol:
				return "NO"

	return "YES"

if __name__ == '__main__':
	main()