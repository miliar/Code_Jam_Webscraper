#!/usr/bin/python

import sys


def policz(tind, lind, tab = 0):
	""" Szuka znaku TOFIND[tind] w LINE za znakiem lind, czyli od lind + 1.
		Rekurencyjnie.
	"""
	global TFIND, LINE, DBG

	if tind >= len(TOFIND):
		if lind <= len(LINE):
			if DBG: print 'oo' * tab, '-> OK return 1'
			return 1
		else:
			if DBG: print '%%' * tab, '-> Error return 0'
			return 0

	counter = 0
	if DBG:
		print '!!' * tab, 'search for "', TOFIND[tind], '" tind =', tind, 'lind =', lind
	newlind = lind
	while True:
		try:
			newlind = LINE.index(TOFIND[tind], newlind)
			if DBG: print '##' * tab, '-> newlind =', newlind, 'in', LINE[lind:]
		except ValueError:
			if DBG: print '##' * tab, '-> ValueError => nie znaleziono znaku w linii'
			break # przerwij petle

		# OK znaleziono znak w LINE
		newlind += 1
		counter += policz(tind + 1, newlind, tab + 1)

		if 0:
			if tind + 1 < len(TOFIND):# nie jest ostatnim znakiem w TOFIND
				counter += policz(tind + 1, newlind, tab + 1)
			else:#if newlind <= len(LINE):#jest ostatnim szukanym znakiem w TOFIND
				counter += 1
				break
	return counter


DBG = 0
TOFIND = 'welcome to code jam'
LINE = ''


if __name__ == '__main__':

	N = raw_input()

	N = int(N)
	for i in range(0, N):
		LINE = raw_input()
		if DBG:
			print '-' * 78
			print 'TOFIND: ', TOFIND, ' len:', len(TOFIND)
			print 'LINE:   ', LINE, ' len:', len(LINE)
			print '        ', ''.join([str(x) for x in range(0, 10)])
		ret = policz(0, 0)
		print 'Case #%d: %s' % (i + 1, str(ret).rjust(4, '0'))

