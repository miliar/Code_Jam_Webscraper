import sys
from sys import argv

def solve(n, k):
	length_dic = {n: 1}
	longest = n
	ans = [None] * 2
	while k > 0 :
		quot = int( (longest - 1)/2 ) 
		res = (longest - 1 ) % 2
		number_of_longest = length_dic[longest]
		length_dic[ quot + res ] = length_dic.get( quot + res , 0) + number_of_longest
		length_dic[ quot ] = length_dic.get( quot, 0 ) + number_of_longest
		k = k - number_of_longest
		del length_dic[longest]
		longest = max( k for k, v in length_dic.items() if v!= 0)
#		print(length_dic, longest, k)
		ans = [ quot + res, quot]
	print( ans[0], ans[1] )

T = int(input())
for i in range(0, T):
	[N, K] = list(map(int, input().strip().split(' ')))
	print("Case #",i+1,": ",sep="",end="")
	solve(N, K)
