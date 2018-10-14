T=int(raw_input())
for t in range(1,T+1):
	print "Case #%d:"%t,
	A,B,K=map(int,raw_input().split())
	A_arr,B_arr,K_arr=range(A),range(B),range(K)
	x= [i&j for i in A_arr for j in B_arr if i&j < K]
	print len(x)
