from __future__ import division

import fileinput
import math
import sys

def debug(s):
	#print >> sys.stderr, "* %s" % s
	#sys.stderr.flush()
	pass

count = int(raw_input())
case = 0

def solve(camStartsAndEnds, aCam, aJam, combined):

	camTime = sum(x[1] - x[0] for x in aJam)
	jamTime = sum(x[1] - x[0] for x in aCam)

	# Walk through the timeline
	lastBusyGuy = not camStartsAndEnds
	lastGuyEndedAt = 0
	switchCount = 0
	leeway = 0
	extraTimes = []
	for c in combined:
		start, end, camIsBusy = c
		if lastBusyGuy == camIsBusy:
			t = start - lastGuyEndedAt
			extraTimes.append((t, camIsBusy))
			if camIsBusy:
				jamTime += t
			else:
				camTime += t
		else:
			switchCount += 1
			leeway += start - lastGuyEndedAt
		lastBusyGuy = camIsBusy
		lastGuyEndedAt = end

	# handle the end
	if lastBusyGuy == camStartsAndEnds:
		# there must be another switch
		switchCount += 1
		leeway += 24 * 60 - lastGuyEndedAt
	else:
		t = 24 * 60 - lastGuyEndedAt
		extraTimes.append((t, lastBusyGuy))
		if lastBusyGuy:
			jamTime += t
		else:
			camTime += t

	extraTimes.sort(key=lambda x: -x[0]) # sort times desc

	debug("camTime: %s" % camTime)
	debug("jamTime: %s" % jamTime)
	debug("leeway: %s" % leeway)
	debug("extraTimes: %s" % extraTimes)

	# step 1: try to assign leeway to get both to 720
	if max(0, 720 - camTime) + max(0, 720 - jamTime) <= leeway:
		return switchCount

	# step 3: assign extraTime
	camNeedsExtraTime = (camTime + leeway < 720)
	debug("need extra time! is it cam? %s" % camNeedsExtraTime)
	timeNeeded = 720 - leeway - (camTime if camNeedsExtraTime else jamTime)
	extraTimesAvailable = [x for x in extraTimes if x[1] == camNeedsExtraTime]
	for t in extraTimesAvailable:
		debug("need extra time!")
		switchCount += 2
		timeNeeded -= t[0]
		if timeNeeded <= 0:
			return switchCount
	return None

while True:
	case += 1
	if count < case:
		break

	combined = []
	Ac, Aj = map(int, raw_input().split())
	aCam = []
	for i in range(Ac):
		start, end = map(int, raw_input().split())
		aCam.append((start, end))
		combined.append((start, end, True))
	aJam = []
	for i in range(Aj):
		start, end = map(int, raw_input().split())
		aJam.append((start, end))
		combined.append((start, end, False))

	# Sort by start times
	aCam.sort(key=lambda x: x[0])
	aJam.sort(key=lambda x: x[0])
	combined.sort(key=lambda x: x[0])

	camStartsResult = solve(True, aCam, aJam, combined)
	jamStartsResult = solve(False, aCam, aJam, combined)
	best = 300
	if camStartsResult is not None:
		best = min(best, camStartsResult)
	if jamStartsResult is not None:
		best = min(best, jamStartsResult)
	debug("results: %s, %s" % (camStartsResult, jamStartsResult))
	print "Case #%s: %s" % (case, best)
