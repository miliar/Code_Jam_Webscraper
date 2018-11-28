T =  int(raw_input())
for t in range(T):
	N, R, O, Y, G, B, V = map(int, raw_input().split())
	
	color = [R, Y, B]
	color.sort ( reverse = True)
	
	if color[1]+ color[2] < color[0]:
		print "Case #%d: %s" % (t+1, "IMPOSSIBLE")
	else:
		color = [(R, "R"), (Y, "Y"), (B,"B")]
		color.sort(reverse=True)
		
		ans = (color[0][1]+color[1][1]+color[2][1])*(color[1][0]+color[2][0] - color[0][0])
		
		#print ans
		ans +=  (color[0][1]+color[1][1])*(color[0][0]-color[2][0])
		#print ans
		ans +=  (color[0][1]+color[2][1])*(color[0][0] - color[1][0])
	
	

		print "Case #%d: %s" % (t+1, ans)
