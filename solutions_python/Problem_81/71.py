#!/usr/bin/env python
# -*- coding: utf8 -*-

__author__    = "renaud blanch <rndblnch at gmail dot com>"
__copyright__ = "Copyright © 2011 - Renaud Blanch"
__licence__   = "GPLv3 [http://www.gnu.org/licenses/gpl.html]"

from common import nt, ni, nl, line


"""
Title
"""

_wp = {}
def wp(score):
	key = "".join(score)
	try:
		return _wp[key]
	except:
		pass

	w, n = 0., 0.
	for c in score:
		if c == '.':
			continue
		n += 1
		if c == '1':
			w += 1
	_wp[key] = wp = w/n
	return wp


_owp = {}
def owp(i, scores):
	key = i, "".join(scores)
	try:
		return _owp[key]
	except:
		pass

	swp, n = 0., 0.
	for j, c in enumerate(scores[i]):
		if c == '.':
			continue
		scorej = list(scores[j])
		scorej[i] = '.'
		swp += wp(scorej)
		n += 1
	_owp[key] = owp = swp/n
	return owp


_oowp = {}
def oowp(i, scores):
	key = i, "".join(scores)
	try:
		return _oowp[key]
	except:
		pass

	sowp, n = 0., 0.
	for j, c in enumerate(scores[i]):
		if c == '.':
			continue
		sowp += owp(j, scores)
		n += 1
	_oowp[key] = oowp = sowp/n
	return oowp


def rpi(i, scores):
	return .25*wp(scores[i]) + .5*owp(i, scores) + .25*oowp(i, scores)


T = ni(); nl()
for X in xrange(T):
	print "Case #%s:" % (X+1)
	N = ni(); nl()
	scores = []
	for i in xrange(N):
		scores.append(nt()); nl()
	for i in xrange(N):
		print rpi(i, scores)
