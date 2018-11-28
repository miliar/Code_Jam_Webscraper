#! /usr/bin/env python

import datetime

def addtime(t1, t2):
	m = t1.minute + t2.minute
	s = 0
	h = 0
	if m > 59:
		h += 1
		m = m % 60
	h += t1.hour
	h += t2.hour
	if h > 23:
		h = 23
		m = 59
		s = 59
	h = h % 24
	return datetime.time(h, m, s)

def gettimes(s):
	s = s.strip().split()
	times = [datetime.time(*map(int, t.split(':'))) for t in s]
	return times

class Station():
	def __init__(self):
		self.ready = 0
		self.reqd = 0
	def depart(self):
		if self.ready > 0:
			self.ready -= 1
		else:
			self.reqd += 1
	def arrive(self):
		self.ready += 1

class Event():
	def __init__(self, station, evttype, time, T):
		self.station = station
		self.evttype = evttype
		if evttype == Station.arrive:
			time = addtime(time, T)
		self.time = time
	def time(self):
		return self.time
	def __cmp__(evt1, evt2):
		if evt1.time < evt2.time: return -1
		if evt1.time > evt2.time: return 1
		if evt1.evttype == Station.arrive: return -1
		else: return 1

def execevents(events):
	for event in events:
		event.evttype(event.station)

def case(infile):
	T = int(infile.readline())
	h = T / 60
	m = T%60
	T = datetime.time(h, m)
	deps = NA, NB = [int(s) for s in infile.readline().strip().split()]
	events = []
	stns = A, B = Station(), Station()
	for i, stn in enumerate(stns):
		for evtnum in xrange(deps[i]):
			deptime, arrtime = gettimes(infile.readline())
			events.append(Event(stn, Station.depart, deptime, T))
			events.append(Event(stns[i-1], Station.arrive, arrtime, T))
	events.sort(cmp=Event.__cmp__)
	execevents(events)
	return A.reqd, B.reqd

if __name__ == '__main__':
	infile = open('B-large.in')
	N = int(infile.readline())
	for casenum in xrange(N):
		reqdA, reqdB = case(infile)
		print 'Case #%d: %d %d' %(casenum+1, reqdA, reqdB)


