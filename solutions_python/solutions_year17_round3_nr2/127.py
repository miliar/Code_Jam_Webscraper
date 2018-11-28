#!/usr/bin/env python

FILE_NAME_BASE = 'B-small-attempt1'
NUM_PROCESSES = 0
MEM_LIMIT_GB = 1.5 # per worker process
RECURSION_LIMIT = 1000

def parse(inp):
	numC, numJ = (int(x) for x in inp.readline().split())
	activities = tuple(
		tuple(int(x) for x in inp.readline().split()) + (idx < numC,)
		for idx in xrange(numC + numJ)
		)
	return activities,

def solve(activities):
	activities = sorted(activities)
	if len(activities) == 1:
		return 2
	elif len(activities) == 2:
		if activities[0][2] == activities[1][2]:
			if activities[1][1] - activities[0][0] <= 720:
				return 2
			elif activities[1][0] - activities[0][1] >= 720:
				return 2
			else:
				return 4
		else:
			return 2
	else:
		return 'not-small'

	#active = activities[0][2]
	#time = 0
	#schedule = []
	#for start, end, who in activities:
		#if who != active:
			#schedule.append((time, start))
			#active = who
			#time = end
	#if active != activities[0][2]:
		#schedule.append((time, 1440))
	#return schedule

def main():
	import sys
	sys.setrecursionlimit(RECURSION_LIMIT)

	import resource
	soft, hard = resource.getrlimit(resource.RLIMIT_AS)
	resource.setrlimit(resource.RLIMIT_AS, (MEM_LIMIT_GB * 1024 ** 3, hard))

	with open(FILE_NAME_BASE + '.in', 'r') as inp:
		numCases = int(inp.readline())
		inputs = [parse(inp) for _ in xrange(numCases)]

	if NUM_PROCESSES == 0:
		runners = [lambda inp=inp: apply(solve, inp) for inp in inputs]
	else:
		from multiprocessing import Pool
		from signal import SIGINT, SIG_IGN, signal
		pool = Pool(NUM_PROCESSES, signal, (SIGINT, SIG_IGN))
		runners = [pool.apply_async(solve, inp).get for inp in inputs]
		pool.close()

	caseFmt = '%' + str(len(str(numCases))) + 'd'
	progressFmt = '[%s/%s] %%s\n' % (caseFmt, caseFmt)
	with open(FILE_NAME_BASE + '.out', 'w') as out:
		for case, runner in enumerate(runners, 1):
			result = runner()
			out.write('Case #%d: %s\n' % (case, result))
			out.flush()
			sys.stderr.write(progressFmt % (case, numCases, result))

if __name__ == '__main__':
	main()
