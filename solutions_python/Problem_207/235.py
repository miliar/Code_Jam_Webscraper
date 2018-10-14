def solve(N,R,O,Y,G,B,V):
	if max(R,Y,B)>sum([R,Y,B])-max(R,Y,B): return "IMPOSSIBLE"
	if R==max(R,Y,B): return "RYB"*(Y+B-R)+"RY"*(R-B)+"RB"*(R-Y)
	if Y==max(R,Y,B): return "YRB"*(R+B-Y)+"YR"*(Y-B)+"YB"*(Y-R)
	if B==max(R,Y,B): return "BRY"*(Y+R-B)+"BR"*(B-Y)+"BY"*(B-R)

testcase = input()
for i in range(testcase):
    N,R,O,Y,G,B,V = map(int,raw_input().split())
    print "Case #"+str(i+1)+":",solve(N,R,O,Y,G,B,V)
