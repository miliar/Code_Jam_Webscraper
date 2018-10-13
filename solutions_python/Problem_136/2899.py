def main():

	files = ["A-small-attempt0.in","B-large.in","C-small.in","D-small.in"]
	content = file(files[1])
	cases = int(content.readline())
	filename = "outputB-large.txt"
	File = open(filename,'w')

	for i in range(cases):
		C,F,X = map(float,content.readline().strip().split())

		rate = 2.0
		T1 = X/rate
		farm = C/rate
		farm_total = farm
		rate+=F
		T2 = (X/rate) + farm_total

		while(T2 < T1):
			T1 = (X/rate) + farm_total #if we stop getting more farms
			farm = C/rate #time to get next farm 
			farm_total += farm #total time spent getting farms
			rate+=F #rate if we acquire another farm
			T2 = (X/rate) + farm_total #if we get another farm and stop

		File.write("Case #%d: %0.7f\n" % (i+1, T1)) 


main()
