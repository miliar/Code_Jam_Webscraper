import sys

def flip(s, start, k):
	p = s[:start]
	q = s[start:start+k]
	r = s[start+k:]

	l = ""
	for i in q:
		if i=="+":
			l+= "-"
		else:
			l+= "+"
	return p+l+r

def check(series, k):
	i=0
	no_flips = 0
	while True:
		if series[i] =="-":
			# print "- found at ", i
			if (i+k)<=len(series):
				series = flip(series, i, k)
				no_flips += 1
				# print "after fliped :", series
			else:
				return "IMPOSSIBLE"
				break
		if i>= len(series)-1:
			break
		i+=1

	return no_flips

def main():
	file = open(sys.argv[1], "r")
	out = open("out_A", "w")

	T = int(file.readline())
	for i in range(1,T+1):
		series, k= file.readline().split(' ')
		k = int(k)
		ans = check(series, k)
		out_string = "Case #%d: %s\n" % (i, str(ans))
		out.write(out_string)

if __name__ == '__main__':
	main()