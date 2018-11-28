from re import *
from sys import stderr
def readint():
	return int(raw_input())
def readfloat():
	return float(raw_input())
def readarray(N, foo=raw_input):
	return [foo() for i in xrange(N)]
def readlinearray(foo=int):
	return map(foo, raw_input().split())

def NOD(a, b):
	while b:
		a,b = b, a%b
	return a

def gen_primes(max):
	primes = [1]*(max+1)
	for i in range(2, max+1):
		if primes[i]:
			for j in range(i+i, max+1, i):
				primes[j] = 0
	primes[0] = 0
	return [x for x in range(max+1) if primes[x]]

def is_prime(N):
	i = 3
	if not(N % 2):
		return 0
	while i*i < N:
		if not(N % i):
			return 0
		i += 3
	return 1

def get_opponents(data, team):
	r = []
	for i in xrange(len(data)):
		if data[team][i] != '.':
			r.append(i)
	return r

case_number = readint()
import sys
for case in xrange(case_number):
	sys.stderr.write("%d\n" % (case,))
	N = readint()
	data = readarray(N)
	WP = [0]*N
	for team in xrange(N):
		games, wins = 0,0
		for opp in xrange(N):
			if data[team][opp] != '.':
				games += 1
				if data[team][opp] == '1':
					wins += 1
		WP[team] = float(wins) / games
	OWP = [0]*N
	for team in xrange(N):
		opps = get_opponents(data, team)
		owp = 0
		for opp in opps:
			games, wins = 0,0
			for opp2 in xrange(N):
				if opp2 != team:
					if data[opp][opp2] != '.':
						games += 1
						if data[opp][opp2] == '1':
							wins += 1
			#print opp, wins, games
			owp += float(wins) / games
		OWP[team] = owp / len(opps)
		#exit(0)
	OOWP = [0]*N
	for team in xrange(N):
		opps = get_opponents(data, team)
		OOWP[team] = float(sum([OWP[opp] for opp in opps])) / len(opps)
	RPI = [0]*N
	for team in xrange(N):
		RPI[team] = 0.25 * WP[team] + 0.50 * OWP[team] + 0.25 * OOWP[team]
	print "Case #%s:" % (case + 1, )
	for r in RPI:
		print r
