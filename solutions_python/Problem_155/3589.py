

filename = "A-small-attempt2.in"

def solve(cnt,aud):
	standing = 0;
	extra = 0;

	for i in range(0,cnt+1):
		current = int(aud[i]);
		
		if current == 0: continue;
		if (standing >= i):
			standing += current;
		else:
			extra += (i - standing);
			standing += extra;
			standing += current;

		# print "standing %d, extra %d" % (standing,extra)
	return extra;

def main():
	f = open(filename,"r");
	cnt = int(f.readline());
	# print "Test cases count %d" % (cnt);
	n = 0;
	for i in range(0,cnt):
		line = f.readline();
		n,a = line.split(" ");
		n = int(n);

		print "Case #%d: %d" % (i+1,solve(n,a))
		solve(n, a)



if __name__ == "__main__":
	main();
	