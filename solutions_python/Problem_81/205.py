def solveCase(N, data):
	wp = [0 for i in range(N)]
	for i in range(N):
		wp[i] = 0
		count = 0
		for j in range(N):
			if data[i][j] == '1':
				wp[i] += 1
			if data[i][j] != '.':
				count += 1
		wp[i] = float(wp[i])/count
	owp = [[0 for j in range(N)] for i in range(N)]
	for i in range(N):
		for j in range(N):
			if i == j or data[i][j] == '.':
				continue
			wc = 0; count = 0
			for k in range(N):
				if k == i:
					continue
				if data[j][k] == '1':
					wc += 1
				if data[j][k] != '.':
					count += 1
			owp[i][j] = float(wc)/count
	#print owp
	mowp = [ 0 for i in range(N) ]
	for i in range(N):
		count = 0
		for j in range(N):
			if data[i][j] != '.':
				count += 1
		mowp[i] = float(sum(owp[i]))/count
	output = ""
	for i in range(N):
		oowp = 0
		count = 0
		for j in range(N):
			if data[i][j] != '.':
				oowp += mowp[j]
				count += 1
		oowp = float(oowp)/count
		#print "mowp: ", mowp
		#print "oowp: ", oowp
		rpi = .25*wp[i] + .5*mowp[i] + .25*oowp
		output += "%.6f\n" % (rpi)
	return output[:-1]

def main():
	T = input()
	for i in range(T):
		N = input()
		data = []
		for j in range(N):
			data.append(raw_input().strip())
		print "Case #%d:\n%s" % (i+1, solveCase(N, data))
main()

