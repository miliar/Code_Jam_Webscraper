import sys
import math

def main(gcj):
	[r, t] = list(map(int, input().split()))
	n = int((-1 + math.sqrt(1 + 4*(2*t + r*(r-1)))) / 2)
	#print((n, (n-(r-1))/2))
	print("Case #%i: %i" % (gcj+1, (n - (r - 1)) / 2))

T = int(input())
#sys.stdin.read
for gcj in range(T):
	main(gcj)
