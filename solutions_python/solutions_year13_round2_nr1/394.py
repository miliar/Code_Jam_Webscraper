#!/usr/bin/python

cases = int(input())

# If there's an unreachable mote:
# Can add (size-1) to the current size repeatedly until it's bridged
# Can nuke the remainder of the list
# So nuking is the upper limit

# Just maintain both lists and figure out which is lower! Linear time anyway...

# At any point in the list, if it would take more steps to reach here than to delete the rest of the list, delete is
# faster

# initial 2
# 9 16 19 64 80 81
# -> 3 -> 5 -> 9 -> 17 (4 steps)
# absorb 9, 16, 19 (total size 61)
# add one more mote (3+) (5 steps)
# Absorb the rest

# Apparently there's a deeper case?
# Probably something involving multiple step-ups.... 

# The case where it would have been cheaper not to step up to the previous mote...

# initial 2
# 1 1 5  15 50
# 3 4 ^7 

for case in range(1, cases + 1):
	initial, n_motes = map(int, input().split())
	initial2 = initial
	motes = list(map(int, input().split()))
	motes.sort()
	motes_steps = [-1 for x in motes]
	steps = 0


	for idx, m in enumerate(motes):
		#print("i: %s m: %s" % (initial, m))
		if m < initial:
			initial += m
			motes_steps[idx] = steps
			continue
		abort = 0
		prev_steps = steps
		while m >= initial:
			#print(initial)
			initial += (initial - 1)
			steps += 1
			# Abort because it's cleary easier to just remove the list
			if steps > prev_steps + len(motes) - idx:
				steps = prev_steps + len(motes) - idx
				#steps = prev_steps + len(motes) - idx
				abort = 1
				break
		initial += m

		best_i = idx
		best_s = steps
		for x in range(idx):
			if motes_steps[x] + len(motes) - x < best_s:
				best_s = motes_steps[x] + len(motes) - x
				best_i = x
		if best_i != idx:
			steps = best_s
			#print("Best at %s" % best_i)
			abort = 1
		if abort:
			#print("Early abort")
			break
		motes_steps[idx] = steps

	# Ewww... but this is definitely causing problems
	if steps > len(motes):
		#print("WTF!!!!")
		#print(initial2)
		#print(motes)
		steps = len(motes)

	#steps = len(motes)
	#for idx, m in enumerate(motes_steps):
	#	if m != -1 and m < len(motes) - idx:
	#		steps = len(motes) - m
	#print(motes_steps)
	print("Case #%s: %s" % (case, steps))
