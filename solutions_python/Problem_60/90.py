import sys

in_file = open(sys.argv[1])
out_file = open("out.txt", 'w')

C = int(in_file.readline().strip())
for c in range(C):
	N, K, B, T = (int(x) for x in in_file.readline().strip().split())
	chick_d = [int(x) for x in in_file.readline().strip().split()]
	chick_v = [int(x) for x in in_file.readline().strip().split()]
	if K == 0:
		result = "0"
	else:
		making_it = 0
		needs_to_be_passed = 0
		passes = 0
		for n in range(N-1, -1, -1):
			if chick_d[n] + chick_v[n] * T >= B:
				passes += needs_to_be_passed
				making_it += 1
				if making_it >= K:
					result = str(passes)
					break
			else:
				needs_to_be_passed += 1
		else:
			result = "IMPOSSIBLE"
	output = "Case #%d: %s\n" % (c+1, result)
	print output,
	out_file.write(output)