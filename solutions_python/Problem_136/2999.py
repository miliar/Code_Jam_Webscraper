# Function
def read_my_file(filename):
    with open(filename, 'r') as f:
        T = int(f.readline())
        output = open("B-large.out", "w")
        for t in range(T):
	        C, F, X = (f.readline()).split()
	        C = float(C)
	        F = float(F)
	        X = float(X)
	        output.write("Case #%d: " % (t+1))
	        
	        rate = float(2)
	        total_time = 0
	        while (X/rate > X/(rate+F) + C/rate):
	        	total_time +=C/rate
	        	rate +=F
	        total_time += X/rate

	        # print("Case #%d: %.7f" % ((t+1), total_time))
	        output.write("%.7f\n" % total_time)


# Python note:
if __name__ == '__main__':
    read_my_file('B-large.in')