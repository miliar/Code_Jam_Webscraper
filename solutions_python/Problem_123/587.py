def main():
	with open('A-small-attempt0.in', 'r') as f:
		line = f.readline()
		ncase = int(line.strip())
		for casenum in range(1, ncase+1):
			arminSize, nmotes = f.readline().split()
			arminSize, nmotes = int(arminSize), int(nmotes)
			motesStr = f.readline().split(' ', nmotes)
			motes = []
			for mote in motesStr:
				motes.append(int(mote))

			print "Case #%d: %d" % (casenum, solve(arminSize, sorted(motes), casenum))
			


def solve(arminSize, motes, casenum, operations=0, action=None):
	# import pdb; pdb.set_trace()
	# print arminSize, motes
	if action:
		operations += 1
		if action == 'add':
			# print "adding", arminSize-1
			motes.insert(0, arminSize-1)
		elif action == 'remove':
			# print 'removing'
			motes.pop()
	
	if arminSize == 1:
		operations += 1
		motes.pop()
		if motes:
			return solve(arminSize, motes[:], casenum, operations)
	
	if not motes:
		return operations


	while motes:
		smallest = motes[0]
			# print arminSize, motes
		if smallest < arminSize:
			# print 'eating first'
			arminSize += motes.pop(0)
			# print arminSize, motes
		else:
			return min(
				solve(arminSize, motes[:], casenum, operations, 'add'),
				solve(arminSize, motes[:], casenum, operations, 'remove')
				)
	return operations
main()