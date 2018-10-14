def ops_to_target(size, target):
	n_ops = 0
	while size < target:
		size += (size-1)
		n_ops += 1

	return n_ops

def n_ops(my_size, mote_sizes):
	my_size = int(my_size)
	mote_sizes = sorted(mote_sizes)

	n_ops = 0

	it = 0
	while it < len(mote_sizes):
		target = mote_sizes[it]
		if target < my_size:
			my_size += target
		else:
			if my_size > 1:
				if ops_to_target(my_size, target) < len(mote_sizes[it:]):
					mote_sizes.insert(it, my_size-1)
					it -= 1
					n_ops += 1
				else:
					n_ops += 1
			else:
				n_ops += 1

		it += 1


	return str(n_ops)

def main():
	f = open('/Users/alex/Downloads/A-small-attempt3.in.txt')
	# f = open('/Users/alex/Downloads/test.in.txt')
	nTests = int(f.readline().replace("\n",""))

	for i in range(nTests):
		line = f.readline().replace("\n","")
		my_size = line.split(" ")[0]
		n_motes = line.split(" ")[1]
		mote_line = f.readline().replace("\n","")

		mote_strs = mote_line.split(" ")
		mote_sizes = []
		for mote in mote_strs:
			mote_sizes.append(int(mote))

		print "Case #" + str(i+1) + ": " + str(n_ops(my_size, mote_sizes))


if __name__ == "__main__":
    main()