def solver():
	rate = 2.0
	c, f, x = [float(i) for i in input().split()]
	maxTime = x / rate
	spent = 0
	while True:
		spent += c / rate
		if spent + x / (rate + f) > maxTime:
			break
		rate += f
		maxTime = spent + x / rate
	return maxTime

def main():
	t = int(input())
	for i in range(1, t + 1):
		solution = solver()
		print("Case #{:d}: {:.7f}".format(i, solution))

if __name__ == "__main__":
	main()	
		