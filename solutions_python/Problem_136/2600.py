def main():
	T = int(raw_input())
	out_file = open("out_cookie_big.txt", 'w')
	for i in xrange(T):
		prod_rate = 2.0
		prod_time = 0.0
		C, F, X = map(float, raw_input().split())
		while buy_farm(C, F, X, prod_rate):
			prod_time += C/prod_rate
			prod_rate += F
		prod_time += X/prod_rate
		out_file.write("Case #%d: %.7f\n" % ((i+1), float(prod_time)))
	out_file.close()

def buy_farm(C, F, X, prod_rate):
	if X/(prod_rate + F) < (X - C)/prod_rate:
		return True
	return False


if __name__ == "__main__":
	main()